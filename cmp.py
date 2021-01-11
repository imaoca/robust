#!/usr/bin/python3

import hashlib
import os

filepath_list = []

received_list = []
for file in os.listdir("./data"):
    filepath = os.path.join("./data", file)
    if os.path.isfile(filepath):
        filepath_list.append(filepath)
        with open(filepath, mode='rb') as f:
            received_list.append(hashlib.md5(f.read()).hexdigest())

check_list = []
with open("check.md5", mode='r') as f:
    for line in f:
        check_list.append(line.split()[0])

OK_count = 0
FAILED_count = 0
DUP_count = 0
used = [False] * len(check_list)
for i, received in enumerate(received_list):
    if received in check_list:
        index = check_list.index(received)
        if not used[index]:
            print(f"OK: {filepath_list[i]}")
            OK_count += 1
            used[index] = True
        else:
            print(f"DUPLICATED: {filepath_list[i]}")
            DUP_count += 1
    else:
        print(f"FAILED: {filepath_list[i]}")
        FAILED_count += 1

print(f"OK = {OK_count}, FAILED = {FAILED_count}, DUP = {DUP_count}")
