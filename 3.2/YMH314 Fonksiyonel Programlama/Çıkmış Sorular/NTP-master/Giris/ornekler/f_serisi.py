# -*- coding: utf-8 -*-
"""
Bu program verilen n sayısına göre
f=1+2+4+...+2^n serisini hesaplar
"""


f=0
n=3
for i in range (n):
    f+=2**i
    print f

print "sonuc=",f