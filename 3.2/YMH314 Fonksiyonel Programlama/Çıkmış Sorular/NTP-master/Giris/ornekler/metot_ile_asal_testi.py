#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:49:22 2018
Metot kendisine gelen sayı asal ise True döndürecek
parametre verilmez ise default değer 2 alınacak
@author: sntr
"""

def asalmi(x=2):
    asal=True
    for i in range(2,(x/2) +1):
        if x%i==0:
            asal=False
            break
    return asal


x=107
if asalmi(x):
    print x,"asal sayidir"
else:
    print x,"asal değildir"



print asalmi()     #Parametresiz çağrılınca x=2 default değer geçerli olacak