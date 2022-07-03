#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:01:41 2018
Liste üretme örnekleri
1,4,9,16,25 ... n^2 serisinden oluşan bir liste üretmek
@author: sntr
"""


"""
#1.yol
x=[]

for i in range(100):
    x.append(i**2)

"""


#2.yol
x=[i**2 for i in range(100)]



print x