# -*- coding: utf-8 -*-
"""
Bu program verilen n sayısına göre
f=1/1+1/2+1/4+...+1/(2^n) serisini hesaplar
f toplamında 1./(2**i) işlemde yuvarlatma yapılmaması
double olarak işlem yapması içindir
"""


f=0.0
n=10
for i in range (n):
    f+=1./(2**i)
    print f

print "sonuc=",f