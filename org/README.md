# 運営用ドキュメント

**Files inside this folder is for the organizers (trainer / tutors). Students does not need to care about them.**

## 競技の直前・競技中に行うべきこと

### 他のユーザーのプロセスを全てkill

競技の直前はもちろん、競技中も他グループのユーザーを `watch 'ps aux | grep group'` 等で確認したらkillすると良い。

```
sudo killall -u group2;sudo killall -u group3;sudo killall -u group4;sudo killall -u group5;
```

### チート対策

競技中に参加者が何らかの不正行為（チート）を行っていないか確認すると良い。具体的には `ready.sh` と `cmp.py` のハッシュ値の確認やソースコードにJammerを経由しない通信に用いるIPアドレスが含まれていないか確認することなどが挙げられる。（回避しようと思えば簡単に回避できるチェック方法なので、より抑止力を持った手法について検討しなければならないかもしれない。）

```
# eb76c7a2b077eebabb112a7f6cba265298c64e692d498dd2cc191a0cba863fb5  ready.sh
# 6b6cdc79159b87bfe2750ce2c6e495453b03337106e2cf7450add4431ea22631  cmp.py
sha256sum ready.sh
sha256sum cmp.py

# 192.168.3 を含むファイルを検索する
find ./ -type f | xargs grep 192.168.3
```

## ファイル

### jammer.c

ジャマ―を実行するためのプログラムのソースコード。以下のようにしてコンパイルして実行しましょう。

```
# WiringPiのダウンロード・インストール
$ wget https://project-downloads.drogon.net/wiringpi-latest.deb
$ sudo dpkg -i wiringpi-latest.deb
# コンパイル・実行
$ gcc -Wall -o jammer jammer.c -lwiringPi
$ ./jammer
```

### jammer.bash

**注意：現在は使われていません。**

ジャマーを実行するためのBashスクリプト。 `jammer.c` への移行に伴い使われなくなりました。実行するにはroot権限が必要です。

```sh
# 実行例
$ sudo bash ./jammer.bash
```

### setupEth0.sh / setupEth1.sh

`eth0` , `eth1` の通信方式・通信速度を競技用に変更するスクリプトです。
