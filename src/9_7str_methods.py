#!/usr/bin/python
# Filename: str_methods.py

#name = 'Swaroop' # This is a string object

name = raw_input('Please input your string')

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'
else:
    print 'No, the staring starts without SWA'

if 'a' in name:
    print 'Yes, it contains the string "a"'
else:
    print 'OOPS, no A'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'
else:
    print 'NO, no WAR here'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

