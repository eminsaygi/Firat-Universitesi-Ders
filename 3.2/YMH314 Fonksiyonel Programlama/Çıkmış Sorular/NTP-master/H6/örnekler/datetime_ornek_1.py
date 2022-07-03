#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr
Tarih, localization
"""

import datetime
import locale

locale.setlocale(locale.LC_ALL,'tr_TR') #yada ''turkish şeklinde yazılabilir

gun=18

ay=3

yil=2018

#Değişkenlerden tarih oluşturma
tarih=datetime.date(yil,ay,gun) # yil-ay-gün şeklinde olmalı sıra
#tarih=datetime.datetime.today() #Bugün

#tarih.year, tarih.month, tarih.day şeklinde de erişilebilir

print tarih

print datetime.datetime.strftime(tarih,"%d %B %A %Y") #Formatlı yazdırma


#Başka dillerde yazdırma
diller=['es_ES.UTF-8','fr_FR.UTF-8','it_IT.UTF-8','ru_RU.UTF-8']
for dil in diller:
    locale.setlocale(locale.LC_TIME,dil)
    print datetime.datetime.strftime(tarih,"%d %B %A %Y") 
    