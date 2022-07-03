#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Python 
liste(list), demet(tuple), küme(set) veri yapıları
ve aralarındaki temel farklar
@author: sntr
"""


liste=[3,1,"b",5,"a",10,2,3,5]    #Tamamen dinamiktirler
demet=(3,1,5,"a",10,2,3,5)        #Sonradan değiştirilemezler
kume={3,1,5,10,2,3,5}             #Çift eleman içermezler


print "Tipler=>",type(liste),type(demet),type(kume)

liste.pop()     #Son elemanı çek
liste.append(20)  #20 yi ekle
liste.sort()    #Listeyi sırala

# Liste üzerinde döngü
print "Liste"
for i in liste:
    print i

# demet.append(3) Hata verecektir çünkü demetlerde günceleme
# Demet üzerinde döngü
print "Demet"
for i in demet:
    print i


#Kümeler üzerinde güncelleme yapabiliriz ama çift değer içermezler
kume.pop()
kume.add("b")   #Kümeye add ile eleman ekliyoruz
# Küme üzerinde döngü
print "Küme"
for i in kume:
    print i