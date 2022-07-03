#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
2-100 arasındaki asal sayıları bulur
for-else yapısı kullanıldı
bayrak değişkeni kullanımına gerek yok
"""

for x in range(2,100):
    for i in range(2,x-1):
        if x%i==0:
            break
    else:
        print x