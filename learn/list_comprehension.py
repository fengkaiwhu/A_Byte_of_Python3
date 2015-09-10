#!/usr/bin/env python
# coding=utf-8
# Filename: list_comprehension.py

listone = [1, 2, 3, 4, 5, 6]
listtwo = [2 * i for i in listone if i > 2 and i < 5]
print(listtwo)
