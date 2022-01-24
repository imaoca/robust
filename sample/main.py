import sys
# import threading
import utils
from scu import SCU

def main():
    if sys.argv[1] == "sender":
        scu = SCU(mtu=1500)
        scu.bind_as_sender(receiver_address=("169.254.229.153", 8888))
        try:
            # serial
            for id in range(0, 1000):
                scu.send(f"../data/data{id}", id)
                print(f"file sent: {id}", end="\r")

            # parallel
            # threads = []
            # for id in range(0, 1000):
            #     threads.append(threading.Thread(target = scu.send(f"../data/data{id}", id)))
            #     threads[-1].setDaemon(True)
            #     threads[-1].start()

            # for th in threads:
            #     th.join()
        except Exception as e:
            print(e)
            scu.drop() # なくても大丈夫だとは思うけど一応安全のため

    elif sys.argv[1] == "receiver":
        # TODO
        scu = SCU(mtu = 1500)
        scu.bind_as_receiver(receiver_address = ("169.254.155.219", 8888))
        for i in range(0, 1000):
            filedata = scu.recv()
            utils.write_file(f"../data/data{i}", filedata)
            print(f"file received: {i}", end="\r")

if __name__ == '__main__':
    main()
