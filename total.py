#!/usr/bin/env python
# coding=utf-8
# Filename: total.py

def total(init=4, *numbers, **keywords):
    count = init
    for i in numbers:
        count += i

    for key in keywords:
        count += keywords[key]

    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))
