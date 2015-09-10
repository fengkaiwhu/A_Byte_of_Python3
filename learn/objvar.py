#!/usr/bin/env python
# coding=utf-8
# Filename: objvar.py

class Robot:
    '''Represents a robot, with a name'''
    population = 0

    def __init__(self, name):
        self.name = name
        print('init the robot {0}'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''I am dying'''
        print('{0} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was the last one'.format(self.name))
        else:
            print('There are still {0} robots'.format(Robot.population))

    def sayHi(self):
        '''Greeting by the Robot.

        Yeah, they can do that'''

        print('Greetings, my master call me {0}'.format(self.name))

    @staticmethod
    def howMany():
        '''Prints the current population'''

        print('We have {0} robots'.format(Robot.population))

if __name__ == '__main__':
    droid1 = Robot('R2-D2')
    droid1.sayHi()
    Robot.howMany()

    droid2 = Robot('C-3PO')
    droid2.sayHi()
    Robot.howMany()

    del droid1
    del droid2
    Robot.howMany()
