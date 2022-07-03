#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

Dosya İşlemi 
Dosyaya karakter dizisinden rastgele seçilen bir karakteri ve random bir sayıyı
a=5, b=2 gibi formatla alt alta dosyaya yazar
"""

import random

f=open("odev.txt","w")


urunler=["sut", "su", "soda","ekmek","peynir"]
subeler=["universite", "merkez", "hastane"]

for i in range(1000):
    f.write(random.choice(subeler)+" =>")
    for k in range(4):
        f.write(random.choice(urunler)+":"+str(random.randint(1,10))+" ")
    f.write("\n")

f.close()