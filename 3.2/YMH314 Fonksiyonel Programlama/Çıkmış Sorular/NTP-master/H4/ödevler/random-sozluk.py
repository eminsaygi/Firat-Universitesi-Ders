#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:47:39 2018

@author: sntr
100 adet random 0-9 rakamların kaçar defa geçtiğini tutan sözlük yapısı
x={"0":5,"1":4 ... "9":7} şeklinde tutulacak 
"""


import random

x=dict()

y=[random.randint(0,10) for i in range(100)] # Random listeyi oluşturma

for i in range(10):                          
    x[str(i)]=y.count(i)  #str(i) i sayısını stringe dönüştürür

print y
print x