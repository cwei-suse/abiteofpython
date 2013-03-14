#!/usr/bin/python
# Filename: method.py

class Person:
    def sayHi(self):
        print 'Hello, how are you?'

p = Person()
Person().sayHi()
p.sayHi()

# This short example can also be written as Person().sayHi() 