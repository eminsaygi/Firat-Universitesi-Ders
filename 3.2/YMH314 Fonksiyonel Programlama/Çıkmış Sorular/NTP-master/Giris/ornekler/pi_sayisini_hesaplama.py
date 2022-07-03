#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
22/7 formülünü kullanarak pi sayısınının ilk 100 basamağını hesaplamak
döngü içinde tam boleni basamak olarak alıp, payı güncelliyoruz
"""
pay=22
payda=7
s="3."
bolum=pay/payda
pay=(pay-bolum*payda)*10
for x in range(100):
    bolum=pay/payda
    pay=(pay-bolum*payda)*10
    s+=str(bolum)

print s