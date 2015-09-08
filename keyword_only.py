#!/usr/bin/env python
# coding=utf-8
# Filename: keyword_only.py

def total(init=5, *number, vegetables):
    count = init
    for i in number:
        count += i

    count += vegetables
    return count

print(total(10, 1, 2, 3, vegetables=50))
# print(total(10, 1, 2, 3,50))
