# Frequently Asked Questions

## Where will the payload be corrupted at?

It will be corrupted in the physical layer. As written in [challenger.md](./challenger.md), the Jamming Machine will directly inject electrical noise into the LAN cable when it is activated.

## Can we apply compression / encoding to the given data?

No. Any compressions, changing formats, encoding, etc... of the data is **NOT ALLOWED**.  
(Except in cases where data size is the same, or being bigger when it is transmitted.) 
The purpose of this challenge is to "Design a Robust Protocol that can communicate data even when its connection is unstable".  
Please understand that allowing them will change the goal and meaning of this challenge.

## Can we use external libraries to help with certain parts of the protocol?

Yes!! You are allowed to use any external libraries!!  
(Just be careful about licensing issues, especially if you are making your program publicly available in places such as GitHub after the competition.)

## Do you plan to support new programming languages to implement a protocol?

If there are requests from multiple teams, we may consider adding new languages.

## Is the Jammer on?
You can check by logging into Taro, and execute 

```
$ ping 169.254.229.153
```
Let it run for a while, then check if about 50% of packets are lost. If about 50% of packets are lost, then the jammer is on (sample output shown below).
```
pi@Taro:~ $ ping 169.254.229.153
PING 169.254.229.153 (169.254.229.153) 56(84) bytes of data.
64 bytes from 169.254.229.153: icmp_seq=2 ttl=64 time=0.992 ms
64 bytes from 169.254.229.153: icmp_seq=4 ttl=64 time=0.939 ms
64 bytes from 169.254.229.153: icmp_seq=5 ttl=64 time=0.888 ms
64 bytes from 169.254.229.153: icmp_seq=10 ttl=64 time=0.945 ms
64 bytes from 169.254.229.153: icmp_seq=11 ttl=64 time=0.845 ms
^C
--- 169.254.229.153 ping statistics ---
15 packets transmitted, 5 received, 66.6667% packet loss, time 397ms
rtt min/avg/max/mdev = 0.845/0.921/0.992/0.063 ms
```
If you let ping run for a while (at least 30 seconds), but still get 0% packet loss, the jammer may be down. 
Please contact us so we can turn it on again.

## main.py has 100% accuracy?
There shouldn't be any data loss since [main.py](./main.py) is an example that shows how you can make your protocol robust, so it's adding headers including checksum, ack number, etc... However, it is robust but slow, so we need to come up with a protocol that can send more files within 60 seconds.

## What is the password for sudo?
You can't have root privileges, and is not necessary to use root privileges in this challenge. Also you don't have to touch [jammer.bash](./jammer.bash).

## There is an error "Permission denied (publickey)" when executing XXX
If this error occurs when accessing Hanako -> Taro, you need to add Hanako's pubkey to Taro's `~/.ssh/authorized_keys`

## How do we start building the robust protocol?
You can take a look at [main.py](./main.py), and treat that as a template for building your robust protocol. However, keep in mind that this is robust but very slow, so you will need to make modifications to it.

## Can you give me an explanation of the sample code?
The example code splits the given file into really small size chunks, and sends it to the receiver with header (packet type, id, sequence number). You can read the top of [packet.py](./packet.py) for the structure of the header.
