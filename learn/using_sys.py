#!/usr/bin/env python
# coding=utf-8
# Filename: using_sys.py

import sys
print("The command line argument are:")
for i in sys.argv:
    print(i)

print("\n\nThe pythonpath is {0}".format(sys.path))
