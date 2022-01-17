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
