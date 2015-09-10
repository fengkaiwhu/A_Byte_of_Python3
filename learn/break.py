#!/usr/bin/env python
# coding=utf-8
# Filename: break.py

while True:
    s = input("Enter something:")
    if s == "quit":
        break;
    print("input length is", len(s))

print("done")
