#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:31:37 2018

@author: sntr
Arama Algoritmaları
lineer, ikili
lineer search => sırasız liste üzerinde
binary search => sıralı olduğunu bildiğimiz liste üzerinde çalışacak
"""

def lineer_search(liste,aranan):
    boyut=len(liste)
    for i in range(boyut):
        if aranan==liste[i]:
            return i
    else:
        return 0




def binary_search(liste,aranan):
    indis=len(liste)/2
    if not indis:
        return "Hata"
    elif aranan==liste[indis]:
        return indis
    elif aranan>liste[indis]:
        return indis+binary_search(liste[indis:],aranan)
    elif aranan<liste[indis]:
        return binary_search(liste[:indis],aranan)
    else:
        return 0


liste=range(50)
print binary_search(liste, 45)