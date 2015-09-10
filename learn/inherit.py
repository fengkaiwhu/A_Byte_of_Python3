#!/usr/bin/env python
# coding=utf-8
# Filename: inherit.py


class SchoolMember:

    '''Represents any school member'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        '''Tell people who I am'''
        print('Name:{0}, Age:{1}'.format(self.name, self.age), end=' ')


class student(SchoolMember):

    '''Represents a student'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('marks:{0}'.format(self.marks))


class teacher(SchoolMember):

    '''Represents a teacher'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('salary:{0}'.format(self.salary))

t = teacher('Mrs. Shrividya', 40, 30000)
s = student('Swaroop', 25, 75)

members = [t, s]
for member in members:
    member.tell()  # 在Teacher和Student上都能工作
