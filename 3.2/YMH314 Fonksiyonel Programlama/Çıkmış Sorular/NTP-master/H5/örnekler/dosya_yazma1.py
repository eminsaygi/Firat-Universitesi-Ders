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


harfler="abcdefghijklmnopqrstuvwxyz"   #26 harften oluşan karakter dizisi


f=open("dene.txt","w") #Okuma modu ile dosyayı aç

for i in range(25):
    f.write(str(random.choice(harfler))+"="+str(random.randint(0,10))+"\n")
    

f.close()