#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:52:16 2018

@author: sntr
"""

"""
#Klasik yöntem - Kontrol değişkeni kullanılıyor
x=23
i=1
asal=True
while i<(x/2)+1:
    i+=1
    if x%i==0:
        asal=False
        break

if asal:
    print x,"asal bir sayidir"
else:
    print x,"asal bir sayi degildir"
"""


x=17
i=1
while i<(x/2)+1:
    i+=1
    if x%i==0:
        print x,"asal bir sayi degildir"
        break

else:
    print x,"asal bir sayidir"
