#!/bin/sh

sudo ethtool -s eth1 autoneg on
sudo ethtool -s eth1 autoneg off
sudo ethtool -s eth1 duplex half
sudo ethtool -s eth1 speed 10
