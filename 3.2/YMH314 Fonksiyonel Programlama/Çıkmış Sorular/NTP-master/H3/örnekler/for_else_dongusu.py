#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:14:32 2018
Asal sayi örneği klasik ve for-else ile çözümü
@author: sntr
"""


"""
#Klasik yöntem - Kontrol değişkeni kullanılıyor
x=25

asal=True    #Asal değişkeni kontrol değişkenimiz
for i in range(2,x/2+1):
    if x%i==0:
        asal=False
        break

if asal:
    print x,"asal bir sayidir"
else:
    print x,"asal degildir"
"""

x=25
#Kontrol değişkenine gerek yok
for i in range(2,x/2+1):
    if x%i==0:
        print x,"asal sayi değildir"
        break

else:
    print x,"asal bir sayidir"
