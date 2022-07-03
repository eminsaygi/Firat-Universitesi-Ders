#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:14:52 2018

@author: sntr
Bir listenin tüm elemanlarının küplerini alarak yeni bir liste oluşturmak
"""

#Kısa yol
x=range(10)
y=[i**3 for i in x]
print x
print y


#Uzun yol
"""
x=range(10)
y=list()

for i in x:
    y.append(i**3)
    
print x
print y
"""