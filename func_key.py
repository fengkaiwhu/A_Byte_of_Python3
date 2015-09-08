#!/usr/bin/env python
# coding=utf-8
# Filename: func_key.py

def func_key(a, b=5, c=10):
    print("a is {0}, b is {1}, c is {2}".format(a, b, c))

func_key(3, 7)
func_key(25, c=24)
func_key(c=50, a=100)
