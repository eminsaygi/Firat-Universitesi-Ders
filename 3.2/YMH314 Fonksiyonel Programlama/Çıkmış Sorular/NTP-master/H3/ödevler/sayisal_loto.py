#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Basit bir sayısal loto programı
metota tahmin edilen 6 adet sayı gönderir, metot ta 6 adet sayı tutar ve kaç tahminin uyuştuğunu geri döndürür
"""

import random

def bul(tahminler):
    #Bilgisayarın tuttuğu sayılar
    tutulanlar=[random.randint(1,50) for i in range(6)]
    print "tutulanlar:",tutulanlar
    tahmin=0
    tutan_tahminler=[]
    for i in tahminler:
        if tutulanlar.count(i)>0: #Tutulanlar içinde tahmin içindeki sayı varmı?
            tahmin+=1
            tutan_tahminler.append(i)
    return "tutan tahmin sayisi=",tahmin,"tutan tahminler=",tutan_tahminler

    

tahminler=(1,5,8,13,23,45)
print "tahminler=",tahminler

print bul(tahminler)