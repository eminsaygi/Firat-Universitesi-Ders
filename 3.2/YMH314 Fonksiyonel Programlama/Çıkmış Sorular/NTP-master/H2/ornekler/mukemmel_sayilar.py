#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:53:42 2018
Mükemmel sayı algoritması
1 dahil kendisi hariç çarpanları toplamı kendisine eşit olan sayı mükemmel sayıdır
@author: sntr
"""

x=[]    #Mükemmel sayıları eklemek için boş bir liste oluşturduk

for a in range(2,1000):
    t=0
    for i in range(1,a):
        if a%i==0:
            t+=i
    if t==a:
        x.append(a)


print "2-1000 arasında",len(x),"adet mükemmel sayı var"
print x