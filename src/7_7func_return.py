#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 例7.7 使用字面意义上的语句. return语句用来从一个函数 返回 即跳出函数。我们也可选从函数 返回一个值 
# Filename: func_return.py

def maximum(x, y):
    '''Prints the docstrings function content testing
    
           Filename: func_return.py.'''
    if x > y:
        return x
    else:
        return y

print maximum(2, 3) 
print maximum.__doc__