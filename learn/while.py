#!/usr/bin/env python
# coding=utf-8
# Filename: while.py

number = 23
running = True
while running:
    guess = int(input("please input an int:"))
    if guess == number:
        print("correct!")
        running = False
    elif guess > number:
        print("high")
    else:
        print("low")
else:
    print("while loop is over!")

print("done")
