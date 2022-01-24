# Sample Program (SCU Protocol)

## About

This sample program is example of the way how you can implement protocol that has robustness. It is written in Python (works on 3.x). You (your group) will try to implement protocol that can beat performance of this protocol.

## Details

By running some tests on trial site, you may realize that as packet is large it is more likely to be corrupted by injected electrical shock. SCU Protocol will split file into unit named `MTU` (check `split_file_into_mtu` function inside `utils.py`), and send it with header that has packet type, id, sequence number. Sender-side will send payload (splitted file) with header that has appropriate data on it. Receiver-side will receive packet and send retransmission request to sender-side when it failed to receive specific fragment of the file.

## How to run

```sh
# Run as sender-side
python3 main.py sender

# Run as receiver-side
python3 main.py receiver
```

## Performance

Slow, but no failure and duplicated files :)

- Taro -> Hanako : `OK = 125, FAILED = 0, DUP = 0`
- Hanako -> Taro : `OK = 56, FAILED = 0, DUP = 0`

## Hint to improve this protocol

Read structure of header (explained at top of the `packet.py`), and think if there are field that is not necessary for this challenge.