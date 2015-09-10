#!/usr/bin/env python
# coding=utf-8
# Filename: func_param.py

def max(a, b):
    if a == b:
        print(a, "is equal", b)
    elif a > b:
        print(a, "is max")
    else:
        print(b, "is max")

max(4, 5)
a = 5
b = 9
max(a, b)
