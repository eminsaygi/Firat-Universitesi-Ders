#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:06:56 2018
Liste üreteci ile 1/4, 1/16, 1/36 .. 1/(2n)^2 serisini üretmek
@author: sntr
"""


#Kısa yol
x=[1./i**2 for i in range(1,100) if i % 2==0]
print x


#Uzun yol
"""
x=list()
for i in range(1,100):
    if i%2==0:
        x.append(1./i**2)
    
print x

"""