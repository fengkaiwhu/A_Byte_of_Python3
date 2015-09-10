#!/usr/bin/env python
# coding=utf-8
# Filename: func_doc.py

def printMax(x, y):
    """Prints the max of two numbers.

    the two values must be integers.
    """
    x = int(x)
    y = int(y)
    
    num = x if x > y else y
    print(num ,"is maximum")

printMax(3, 5)
print(printMax.__doc__)
