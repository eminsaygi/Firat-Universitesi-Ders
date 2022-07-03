#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

String her satırı büyük harf yapma ve replace
"""

#Çok satırlı string tanımlama
s="""Python ;
yüksek seviyeli bir programlama dili.
bilim ve teknoloji bilgi sanayesinde önemli rolu var.
uluslar arası alanda etkili.
askeri savunma alanda etkili.
hacking network sistemleri üzerinde etkili.
"""



liste=s.splitlines()

s1=""

for k in liste:
    s1+=k.capitalize()+"\n"
    

s1=s1.replace("Python", "Python programlama dili")
print s1