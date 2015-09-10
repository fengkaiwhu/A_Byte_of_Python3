#!/usr/bin/env python
# coding=utf-8
# Filename: addr_book.py

class addr_book:
    '''Represent an addr_book'''
    
    book = {}

    def __init__(self, book):
        addr_book.book = book

    def get_book(self):
        return addr_book.book

    def add_person(self):
        name = input('Please input name-->')
        address = input('Please input address-->')
        phone = input('Please input phone-->')

        from person import person
        person = person(name, address, phone)

        if person.name in addr_book.book.keys():
            print('The person already exists')
        else:
            addr_book.book[person.name] = person
        
        del person

    def del_person(self):
        name = input('Please input name-->')
        if name not in addr_book.book.keys():
            print('The person is not exists')
        else:
            addr_book.book.pop(name)

    def modify_person(self):
        name = input('Please input name-->')
        if name not in addr_book.book.keys():
            print('The person is not exists')
        else:
            person = addr_book.book[name]
            print('Original infomation Name: {0}, address: {1}, phone: {2}'.format(name, person.address, person.phone))
            person.name = input('Please input new name-->')
            person.address = input('Please input new address-->')
            person.phone = input('Please input new phone-->')

    def show_person(self):
        if len(addr_book.book.keys()) == 0:
            print('Address book is empty.')
        else:
            for name, person in addr_book.book.items():
                print('Name: {0}, address: {1}, phone:{2}'.format(person.name, person.address, person.phone))

if __name__ == '__main__':
    addr_book = addr_book()
    addr_book.add_person()
