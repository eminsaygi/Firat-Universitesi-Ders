#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

Dosya İşlemi 
yazma modu ile dosya açıp içine 1-100 sayılarını alt alta yazıyoruz
programdan sonra deneme.txt kontrol ediniz

Dosya okuma işlemi istisna işleme ile birlikte yapılmıştır
"""

print "Dosya Okuma "

try:
    f=open("deneme.txt","r") #Okuma modu ile dosyayı aç
    #Dosyayı değiştirerek istisna üretip mesajı görün
    #Dosya yetkisini Windows ortamında el ile değiştirerek örneğin salt okunur yaparak, yazma modunda açmayı deneyin

    a=f.readlines()  #Satır satır listeye at
    t=0
    for i in a:
        t+=int(i)   #Satırı int e dönüştür
        
    print "Dosyadaki sayilarin toplami=",t

    
except Exception as e:  #Exception süper sınıfını kullandık (İstisna türünü bilmediğimizi varsaydık)
    print "Bir hata oluştu orjinal hata mesaji=",e
    print "Hatanin sinifi=",e.__class__ #Bu örnekte exception sınıfı IOError olarak görülecektir, aşağıda verilmiştir

finally:
    print "Dosya kapatiliyor"
    f.close()  


"""
except IOError:
    print "IO Hatasi"
"""