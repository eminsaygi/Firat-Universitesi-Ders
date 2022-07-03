#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:39:58 2018
Python sözlük veri yapısı
@author: sntr
"""

sozluk={"isim":"Python", "dogumyili":"1990","nesne":True,"versiyon":3}

#Sözlük üzerinde döngü
print "tipi=",type(sozluk)

for (k,v) in sozluk.items():
    print k,"=>",v


print sozluk["versiyon"]          #Spesifik bir anahtarın değerine erişmek
sozluk["gelistirici"]="Rossum"    #Yeni key:value ilave etmek
sozluk["dogumyili"]="1991"  

print sozluk            #Sözlüğü tek seferde yazdırmak
print len(sozluk)     
  
print sozluk.keys()
print sozluk.values()
