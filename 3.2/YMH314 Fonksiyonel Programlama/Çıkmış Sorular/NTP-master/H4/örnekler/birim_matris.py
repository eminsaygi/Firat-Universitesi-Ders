#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:18:29 2018

@author: sntr
nxn Birim matris oluşturma
"""

n=5
x=list()
for i in range(n):
    y=list()
    for j in range(n):
        y.append(1) if i==j else y.append(0)  # if-else satır içi kullanımı
    x.append(y)
    

for i in x:
    print i