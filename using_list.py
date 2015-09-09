#!/usr/bin/env python
# coding=utf-8
# Filename: using_list.py

shoplist = ['apple', 'mongo', 'carrot', 'banana']
print("I have {0} items to purchase".format(len(shoplist)))

print("These items are:", end='')
for item in shoplist:
    print(item, end=' ')

shoplist.append('rice')
print('\nMy shoplist is now {0}'.format(shoplist))

shoplist.sort()
print('My sorted shoplist is now {0}'.format(shoplist))
fisrtitem = shoplist[0]
del shoplist[0]
print("I bought the {0}, my shoplist is now {1}".format(fisrtitem, shoplist))

