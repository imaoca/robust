#!/bin/bash
trap 'echo "wait a moment..."; echo 17 > /sys/class/gpio/unexport; sleep 5; echo "cleaned gpio17."; exit 0;' 2
echo 17 > /sys/class/gpio/unexport
echo 17 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio17/direction
while true
do
  sleepenh `printf 0.0%03d $((150 + $RANDOM % 100))`
  echo 1 > /sys/class/gpio/gpio17/value
  sleepenh `printf 0.0%03d $((150 + $RANDOM % 100))`
  echo 0 > /sys/class/gpio/gpio17/value
done
