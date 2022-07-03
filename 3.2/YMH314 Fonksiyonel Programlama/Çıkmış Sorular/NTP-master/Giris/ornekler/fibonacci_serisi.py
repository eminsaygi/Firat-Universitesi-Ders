#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
ilk 100 fibonacci sayısını yazdırma
"""
a=1
b=2 #sıradaki fibonacci sayısı
for x in range(100):
    c=a+b
    a,b=b,c  #çoklu atama
    print c
