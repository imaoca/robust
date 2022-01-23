# 運営用ファイル

**Files inside this folder is for the organizers (trainer / tutors). Students does not need to care about them.**

## jammer.bash

ジャマーを起動するためのBashスクリプト。実行するにはroot権限が必要です。

```sh
# 実行例
sudo nohup bash ./jammer.bash &
```

## setupEth0.sh / setupEth1.sh

`eth0` , `eth1` の通信方式・通信速度を競技用に変更するスクリプトです。