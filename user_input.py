#!/usr/bin/env python
# coding=utf-8
# Filename: user_input.py

def reverse(text):
    return text[::-1]

def ispalindrome(text):
    return text == reverse(text)

something = input('Input something-->')

if ispalindrome(something):
    print('Yes, it is a palindrome.')
else:
    print('No, it is not a palindrome.')
