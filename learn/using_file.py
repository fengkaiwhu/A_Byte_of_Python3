#!/usr/bin/env python
# coding=utf-8
# Filename: using_file.py

peom = """Programming is fun
When the work is done

if you wanna make your work also fun
    use python
"""

f = open('peom.txt', 'w')
print(f)
f.write(peom)
f.close()
f = open('peom.txt', 'rb')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)

f.close()
'''
with open('peom.txt') as f:
    print(f)
    for line in f:
       print(line)
'''
