# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:52:50 2018

@author: FeyzaÖzbay
"""
dosya = open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\sayi1.txt","r")
sayilar = [int(satir) for satir in dosya.readlines()]
dosya.close() # artik dosyayla isimiz bittigine gore kapatabiliriz.
print ("Sayilar\n")
print (sayilar)
dosya3=open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\ciftsayilar.txt","w") #Yazma modu ile dosyayı
dosya4=open("C:\\Users\\FeyzaÖzbay\\Documents\\Python\\teksayilar.txt","w") #Yazma modu ile dosyayı
for i in range(10):
   if sayilar[i] % 2 == 0:
      dosya3.write(str(sayilar[i])+"\n")
   else:
      dosya4.write(str(sayilar[i])+"\n")
dosya3.close()
dosya4.close()