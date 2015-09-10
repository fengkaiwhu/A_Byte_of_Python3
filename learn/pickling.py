#!/usr/bin/env python
# coding=utf-8
# Filename: pickling.py

import pickle

shoplist = ['apple', 'mango', 'carrot']

f = open('shoplist.data', 'wb')
pickle.dump(shoplist, f)
f.close()

f = open('shoplist.data', 'rb')
print(pickle.load(f))
