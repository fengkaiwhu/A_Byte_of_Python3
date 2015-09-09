#!/usr/bin/env python
# coding=utf-8
# Filename: using_dict.py

ab = {
    "Swaroop":"Swaroop@qq.com",
    "Larry":"Larry@qq.com",
    "Feng":"Feng@qq.com",
    "Spammaer":"Spammaer@qq.com"
}

print("Feng's address is {0}".format(ab['Feng']))

del ab['Larry']

print('\nThere are {0} contacts in the address-book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

ab['Guido'] = 'Guido@qq.com'

if 'Guido' in ab.keys():
    print("Guido's address is {0}".format(ab['Guido']))
