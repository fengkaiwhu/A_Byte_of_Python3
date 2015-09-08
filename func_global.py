#!/usr/bin/env python
# coding=utf-8
# Filename: func_global.py
x = 50

def func():
    global x
    print("x is", x)
    x = 2
    print("change x to", x)

func()

print("x still is", x)
