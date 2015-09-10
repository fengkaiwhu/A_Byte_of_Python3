#!/usr/bin/env python
# coding=utf-8
# Filename: str_methods.py

name = 'Swaproop hello world. my friend'
print(name.isalnum())
print(name.isprintable())
print(name.split())
print(name.rsplit())
print(name.split(sep='o'))
print(name.split(sep='o', maxsplit=2))
print(name[::-1])

mylist = name.split()
dep = '__'
print(dep.join(mylist))

print(name.replace(' ', '__', 2))
