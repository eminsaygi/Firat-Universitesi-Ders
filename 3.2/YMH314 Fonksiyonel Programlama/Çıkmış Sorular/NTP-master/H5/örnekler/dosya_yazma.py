#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

Dosya İşlemi 
yazma modu ile dosya açıp içine 1-100 sayılarını alt alta yazıyoruz
programdan sonra deneme.txt kontrol ediniz
"""



f=open("deneme.txt","w") #Yazma modu ile dosyayı aç

for i in range(100):
    f.write(str(i)+"\n")
    


f.close()  #Dosyayı kapat