#!/usr/bin/env python
# coding=utf-8
# Filename: main.py

import addr_book
import pickle

def flush():
    '''Write data into disk.'''
    with open('addr_book.data', 'wb') as f:
        pickle.dump(addr_book.get_book(), f)

with open('addr_book.data', 'rb') as f:
    try:
        book = pickle.load(f)
    except EOFError:
        book = {}

addr_book = addr_book.addr_book(book)

while True:
    print('*********************************')
    print('Please choose you operation:\n 1. add person\n 2. delete person\n 3. modify person\n 4. show person\n 5. exit ')
    op = input('Choose: ')
    print('*********************************')

    if op == '1':
        addr_book.add_person()
        flush()
    elif op == '2':
        addr_book.del_person()
        flush()
    elif op == '3':
        addr_book.modify_person()
        flush()
    elif op == '4':
        addr_book.show_person()
    elif op == '5':
        break
    else:
        print('Illegal operation!')

