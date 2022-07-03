#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 23:12:32 2018

@author: sntr
"""

import timeit 

def fib1(n):
    return 1 if n<=1  else fib1(n-1)+fib1(n-2)



fib=dict()

def fib2(n):
    if n<=1:
        fib[str(n)]=1
        return 1
    elif fib.has_key(str(n-1)):
        fib[str(n)]=fib[str(n-1)]+fib[str(n-2)]
        return fib[str(n)]
    else:
        return fib2(n-1)+fib2(n-2)
    
    
#print fib2(7)


bas = timeit.default_timer()
print fib2(35)
son = timeit.default_timer()
print son-bas