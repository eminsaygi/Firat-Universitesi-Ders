#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:34:08 2018

@author: sntr
nxn boyutunda 2 matrisi toplama
matrisler metot ile elemanları random olacak şekilde oluşturulacak
"""

n=3
import random

def matris_olustur():
    x=[ [random.randint(1,9) for c in range(n)] for i in range(n)] #Satır içi üreteçle iki boyutlu matris üretme
    return x


def topla(a,b):
    for i in range(n):
        for j in range(n):
            c[i][j]=a[i][j]+b[i][j]
    return c

a= matris_olustur()
b=matris_olustur()
c=matris_olustur()

print a
print b
c=topla(a,b)
print c