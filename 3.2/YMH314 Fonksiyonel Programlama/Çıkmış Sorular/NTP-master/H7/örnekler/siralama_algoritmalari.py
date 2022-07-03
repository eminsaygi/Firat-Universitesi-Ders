#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:31:37 2018

@author: sntr
Sıralama Algoritmaları
"""

#Seçmeli Sıralama
#En küçük elemanı bulur ilk elemanla yer değiştirir
#Kalan elemanlar için işlem tekrarlanır
# N(N-1)/2
def selection_sort(liste):
    boyut = len(liste)
    for i in range(boyut):
        son = i
        for k in range(i + 1, boyut):
            if liste[k] < liste[son]:
                son = k
        liste[son], liste[i] = liste[i], liste[son]
        #print liste
    return liste


#Eklemeli Sıralama
#Dizinin ilk elemanı kalan elemanlar ile karşılaştırılır daha küçükse dizi ötelenerek yer değiştirilir
#2(1+2+...+(N-2)+(N-1))=N(N-1)
def insertion_sort(liste):
    boyut = len(liste)
    for i in range(1, boyut):
        while 0 < i and liste[i] < liste[i - 1]:
            liste[i], liste[i - 1] = liste[i - 1], liste[i]
            i -= 1
        #print liste
    return liste


#Kabarcık Sıralama
#Her eleman bir sonraki ile karşılaştırılır, gerekirse yer değiştirilir
#(N-1)(N-1)
def bubble_sort(liste):
    boyut = len(liste)
    for i in range(boyut):
        for j in range(boyut-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
        #print liste
    return liste

#Hızlı Sıralama
#pivot seçilir, büyükler sağa, küçükler sola eklenir, rekürsif olarak devam eder
#n(log2n), en kötü durumda n^2
def quick_sort(liste):
    boyut = len(liste)
    if(boyut <= 1):
        return liste
    else:
        pivot = liste[0]
        buyuk = [ element for element in liste[1:] if element > pivot ]
        kucuk = [ element for element in liste[1:] if element <= pivot ]
        return quick_sort(kucuk) + [pivot] + quick_sort(buyuk)


liste=[19,2,31,45,6,11,121,27]

print (quick_sort(liste))
