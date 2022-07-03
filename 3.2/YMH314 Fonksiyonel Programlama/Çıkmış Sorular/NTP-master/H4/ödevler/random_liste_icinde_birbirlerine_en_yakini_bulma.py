#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:54:31 2018

@author: sntr
100 adet random sayıdan birbirlerine en yakın olanı bulma (farkları minumum olanlar)
"""


import random

sayilar=list()
minimum=1 #minimum değişkeninin başlangıç değeri
liste=[random.random() for i in range(100)] # Random listeyi oluşturma

for x in liste[0:len(liste)-1]:                      #Her sayıyı listedeki bir sonraki sayı ile karşılaştırıyoruz
    for y in liste[(liste.index(x)+1):len(liste)]:   #Karşılaştırma işlemi listenin sonuna kadar her eleman için yapılacak
        if abs(x-y) <minimum:                        #Farkların mutlak değerini alıyoruz
            sayilar[:2]=[x,y]                        
            minimum=abs(x-y)


print "minumum fark=",minimum
print "en yakin sayilar=",sayilar
print "tüm liste=",liste
            
