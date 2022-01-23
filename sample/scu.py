from queue import Queue
import socket
import threading
from enum import Enum

from packet import SCUPacketType, SCUHeader, SCUPacket
import utils

class SCUMode(Enum):
    SendMode = 0
    RecvMode = 1

class SCU:
    def __init__(self, mtu=1500):
        self.mtu = mtu

    def bind_as_sender(self, receiver_address):
        self.mode = SCUMode.SendMode
        self.connection_manager = {}

        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver_address = receiver_address
        self.lock = threading.Lock()

        sender_packet_loop_thread = threading.Thread(target=self._sender_packet_loop)
        sender_packet_loop_thread.setDaemon(True)
        sender_packet_loop_thread.start()

    def bind_as_receiver(self, receiver_address):
        self.mode = SCUMode.RecvMode
        self.received_files_data = {}

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(receiver_address)

        self.file_received = Queue()

        receiver_packet_loop_thread = threading.Thread(target=self._receiver_packet_loop)
        receiver_packet_loop_thread.setDaemon(True)
        receiver_packet_loop_thread.start()

    def drop(self):
        if self.mode == SCUMode.SendMode:
            self.connection_manager.clear()
            self.socket.close()

    def _sender_packet_loop(self):
        if self.mode == SCUMode.RecvMode:
            raise Exception
        while True:
            try:
                packet = SCUPacket()
                packet.from_raw(self.socket.recv(2048))
                if packet.header.id not in self.connection_manager:
                    continue
                if packet.header.typ == SCUPacketType.Fin.value:
                    self.connection_manager[packet.header.id].put((True, packet.header.seq))
                elif packet.header.typ == SCUPacketType.Rtr.value:
                    self.connection_manager[packet.header.id].put((False, packet.header.seq))
            except Exception as e: # recvが失敗した時とputが失敗した時は(適当)
                if e == KeyboardInterrupt:
                    raise KeyboardInterrupt
                else:
                    import traceback
                    traceback.print_exc()

    def send(self, filepath, id): # will lock the thread
        if self.mode == SCUMode.RecvMode:
            raise Exception
        queue = Queue()
        self.connection_manager[id] = queue # コネクションを登録

        data_fragments = utils.split_file_into_mtu(filepath, self.mtu)

        all_packets = []
        for (seq, df) in enumerate(data_fragments):
            # create header
            header = SCUHeader()
            if seq == len(data_fragments) - 1:
                header.from_dict({ "typ": SCUPacketType.DataEnd.value, "id": id, "seq": seq, })
            else:
                header.from_dict({ "typ": SCUPacketType.Data.value, "id": id, "seq": seq, })
            # create packet
            packet = SCUPacket()
            packet.from_dict({ "header": header, "payload": df, })

            all_packets.append(packet)

        retransmit_seq = 0 # 再送の必要があるパケットを管理(どこまで受け取れてるか)
        seq = 0
        while True:
            try:
                while True:
                    try:
                        fin, sq = queue.get(block=False) # 再送要求か受信完了報告か
                        if fin: # 送信完了
                            del(self.connection_manager[id]) # コネクションを解除
                            return
                        elif sq < len(all_packets): # 再送要求
                            retransmit_seq = max(sq, retransmit_seq)
                    except Exception as e: # キューが空の時
                        if e == KeyboardInterrupt:
                            raise KeyboardInterrupt
                        else:
                            break
                with self.lock: # 複数のsendメソッドが並列に同時実行されている可能性があるため，ロックが必要
                    self.socket.sendto(all_packets[seq].raw(), self.receiver_address) # パケット送信

                seq = max(seq + 1, retransmit_seq) # seq更新
                if seq >= len(all_packets):
                    seq = retransmit_seq
            except Exception as e: # sendtoが失敗した時は(適当)
                if e == KeyboardInterrupt:
                    raise KeyboardInterrupt
                else:
                    import traceback
                    traceback.print_exc()



    def _receiver_packet_loop(self):
        if self.mode == SCUMode.SendMode:
            raise Exception
        received_files_flag = {}
        received_files_length = {}
        while True:
            try:
                data, from_addr = self.socket.recvfrom(2048)
                packet = SCUPacket()
                packet.from_raw(data)

                key = utils.endpoint2str(from_addr, packet.header.id)
                if key not in self.received_files_data:
                    self.received_files_data[key] = [b""]*100
                    received_files_flag[key] = False

                if received_files_flag[key]:
                    self.response(SCUPacketType.Fin.value, from_addr, packet.header.id, 0)
                    continue

                if packet.header.typ == SCUPacketType.DataEnd.value or packet.header.typ == SCUPacketType.Data.value:
                    if packet.header.typ == SCUPacketType.DataEnd.value:
                        received_files_length[key] = packet.header.seq + 1

                    self.received_files_data[key][packet.header.seq] = packet.payload
                    rtr = self.calculate_rtr(key, packet.header.seq)
                    if rtr is not None: # 再送要求する必要あり
                        self.response(SCUPacketType.Rtr.value, from_addr, packet.header.id, rtr)
                    elif key in received_files_length and self.is_all_received(key, received_files_length[key]): #  ファイル受信完了
                        received_files_flag[key] = True
                        self.response(SCUPacketType.Fin.value, from_addr, packet.header.id, 0)
                        self.file_received.put((key, received_files_length[key]))

            except Exception as e: # recvが失敗した時とputが失敗した時は(適当)
                if e == KeyboardInterrupt:
                    raise KeyboardInterrupt
                else:
                    import traceback
                    traceback.print_exc()

    def calculate_rtr(self, key, seq):
        for sq in range(0, seq):
            if not self.received_files_data[key][sq]:
                return sq
        return None

    def is_all_received(self, key, length):
        for i in range(0, length):
            if not self.received_files_data[key][i]:
                return False
        return True

    def response(self, typ, addr, id, rtr):
        if self.mode == SCUMode.SendMode:
            raise Exception
        if typ == SCUPacketType.Rtr.value:
            header = SCUHeader()
            header.from_dict({ "typ": typ, "id": id, "seq": rtr, })
            packet = SCUPacket()
            packet.from_dict({ "header": header, "payload": b'', })
            self.socket.sendto(packet.raw(), addr)

        elif typ == SCUPacketType.Fin.value:
            header = SCUHeader()
            header.from_dict({ "typ": typ, "id": id, "seq": rtr, })
            packet = SCUPacket()
            packet.from_dict({ "header": header, "payload": b'', })
            self.socket.sendto(packet.raw(), addr)

    def recv(self):
        if self.mode == SCUMode.SendMode:
            raise Exception
        key, length = self.file_received.get()
        return utils.fold_data(self.received_files_data[key], length)

