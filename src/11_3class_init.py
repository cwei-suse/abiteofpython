#!/usr/bin/python
# Filename: class_init.py

class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def sayHi(self):
        print 'Hello, my name is', self.name
        print 'Gender is:', self.sex

p = Person('Swaroop','Male')
p.sayHi()

# This short example can also be written as Person('Swaroop').sayHi() 