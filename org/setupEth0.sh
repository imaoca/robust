#!/bin/sh

sudo ethtool -s eth0 autoneg on
sudo ethtool -s eth0 autoneg off
sudo ethtool -s eth0 duplex full
sudo ethtool -s eth0 speed 10
