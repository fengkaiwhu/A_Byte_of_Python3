#!/usr/bin/env python
# coding=utf-8
# Filename: continue.py

while True:
    s = input("Enter something:")
    if s == "quit":
        break;
    if len(s) < 3:
        print("too short")
        continue;
    print("long!")

print("done")
