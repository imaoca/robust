# Frequently Asked Questions

Please check this page before asking questions to trainer and tutors.

## Where will the payload be corrupted at?

It will be corrupted in the physical layer. Jamming Machine will directly inject electrical noise into the LAN cable when it is activated.

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

## How to check if jammer is running or not?

You can check by logging into Taro, and run following command.

```
$ ping -c 10 169.254.229.153
```

If about 50% of packets are lost, then the jammer is running (sample output shown below).

```
$ ping -c 10 169.254.229.153
PING 169.254.229.153 (169.254.229.153) 56(84) bytes of data.
64 bytes from 169.254.229.153: icmp_seq=1 ttl=64 time=1.70 ms
64 bytes from 169.254.229.153: icmp_seq=4 ttl=64 time=0.902 ms
64 bytes from 169.254.229.153: icmp_seq=6 ttl=64 time=0.861 ms
64 bytes from 169.254.229.153: icmp_seq=8 ttl=64 time=0.872 ms
64 bytes from 169.254.229.153: icmp_seq=9 ttl=64 time=0.839 ms

--- 169.254.229.153 ping statistics ---
10 packets transmitted, 5 received, 50% packet loss, time 245ms
rtt min/avg/max/mdev = 0.839/1.035/1.704/0.336 ms
```

If you run `ping` for a while, but still get 0% packet loss, the jammer may be not running. 
Please contact trainer and tutors so we can run it again.

## Does sample program has 100% accuracy?

There shouldn't be any data loss since sample program is an example that shows how you can make your protocol robust. However, it is slow (cannot transfer much files within 60 seconds), so we need to come up with a protocol that has higher performance.

## What is the password for sudo?

You can not have root privilege on Trial Site.

## There is an error "Permission denied (publickey)" when executing ready.sh on Hanako

You need to add Hanako's SSH public key to Taro's `~/.ssh/authorized_keys`

## How do we start building the robust protocol?

Check "Getting Started" on [README.md](./README.md)

## Can you give me an explanation of the sample code?

Check [README.md](sample/README.md) inside `sample` directory.

## How can I generate SSH key pair for this challenge?

Use `ssh-keygen` command to generate SSH key pair. In default (entering nothing), SSH public key will be placed at `~/.ssh/id_rsa.pub`.
