#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:12:05 2018
1 ile 1000 arasında rastgele sayıda elemandan oluşan, değerleri 0-1 arasında değişen
bir liste oluşturuluyor, ardından eleman sayısı ve toplamı bulunuyor
@author: sntr
"""
import random

liste=list()

for i in range(random.randint(1,1000) ):
    liste.append(random.random())


x,s=len(liste),sum(liste)

print x,"tane elemandan oluşan listenin toplamı=",s,"ortalaması=",s/x