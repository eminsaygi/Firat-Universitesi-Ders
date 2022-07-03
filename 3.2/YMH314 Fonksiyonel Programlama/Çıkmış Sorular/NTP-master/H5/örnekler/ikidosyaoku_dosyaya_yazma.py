# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:52:50 2018

@author: FeyzaÖzbay
"""
dosya = open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\sayi1.txt","r")
sayilar = [int(satir) for satir in dosya.readlines()]
dosya.close() # artik dosyayla isimiz bittigine gore kapatabiliriz.
print (sayilar)
ortalama = sum(sayilar) / len(sayilar) # ortalama almak icin kolay bir yontem!
print (ortalama)
dosya2 = open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\sayi2.txt","r")
sayilar2 = [int(satir2) for satir2 in dosya2.readlines()]
dosya2.close() # artik dosyayla isimiz bittigine gore kapatabiliriz.
print (sayilar2)
ortalama2 = sum(sayilar2) / len(sayilar2) # ortalama almak icin kolay bir yontem!
print (ortalama2)
sayilar3 = list()
for i in range(10):
   sayilar3.append (sayilar[i]+sayilar2[i])
print  (sayilar3)
dosya3=open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\sayi3.txt","w") #Yazma modu ile dosyayı aç
dosya3.write(str(sayilar3)+"\n")
dosya3.close()