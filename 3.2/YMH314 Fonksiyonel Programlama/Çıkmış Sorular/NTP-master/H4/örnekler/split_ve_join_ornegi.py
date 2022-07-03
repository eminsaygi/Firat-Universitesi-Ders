#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:36:07 2018

@author: sntr

#Stringi parse etme ve join etme örneği
"""

st= "Hafta=4, Gun=1, Saat=9, Dakika=3"
#Bu formatı tüm değerleri 1 arttırarak Hafta:5-Gun:2-Saat:10-Dakika:4" formatına çevirecek

print "Orjinal=>",st

st1=st.split(",")  #Önce Virgüle göre ayrıyoruz
print "Virgüle göre parse edilmiş hali=>",st
yeni=""

for i in st1:
    temp=i.split("=")
    yeni+=(temp[0]+":"+str(int(temp[1])+1))          #Bu satırda araya ":" koyarak biz birleştirdik
    #yeni+=':'.join([temp[0],str(int(temp[1])+1)])   #Bu satırda ise join gömülü fönksiyonunu kullandık

    
yeni='-'.join(yeni.split(" ")) # Önce boşluğa göre split et, sonra - ile join et
print "Değiştirilmiş hali =>",yeni