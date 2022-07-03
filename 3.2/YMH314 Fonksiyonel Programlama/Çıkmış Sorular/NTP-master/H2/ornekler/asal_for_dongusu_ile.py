#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
2-100 arasındaki asal sayıları bulur
kontrol değişkenini bayrak olarak kullanıyoruz
döngü başında kontrol=True
içteki döngüde eğer sayı bölünürse kontrol=False yapılarak döngü kırılıyor (break ifadesi)
döngü sonunda kontrol halen True ise sayı ekrana yazdırılıyor
if kontrol: kontrol zaten boolean değişken olduğu için == ile karşılaştırmaya gerek yok
"""

for x in range(2,100):
    kontrol=True
    for i in range(2,x-1):
        if x%i==0:
            kontrol=False
            break
    if kontrol:
        print x