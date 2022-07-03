#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:16:24 2018

@author: sntr
axb, bxc boyutunda iki matrisi çarpma
inline fonksiyon kullanıldı
boyutların uyumu ihmal edilmiştir
"""

n=3
import random

def matris_olustur(x,y):
    x=[ [random.randint(1,9) for c in range(y)] for i in range(x)] #Satır içi üreteçle iki boyutlu matris üretme
    return x


def carp(a,b):
    c=[ [ sum(a[i][k]*b[k][j] for k in range(len(b)) ) for j in range(len(b[0]))] for i in range(len(a))]

    return c

a= matris_olustur(3,2)
b= matris_olustur(2,3)

print a
print b
c=carp(a,b)
print "\n"
print c