#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

Map - Filter - Reduce - Lambda örneği

Listeden çift sayıları süz (filter), karelerini al (map), toplamlarını bul (reduce)
"""

karesi=lambda x: x**2

sec=lambda x: x%2==0

toplam= lambda x,y: x+y

liste=range(50)

suzulen = filter(sec,liste) # =[i for i in liste if i%2==0] #Liste işleci ile
maplenen = map (karesi,suzulen) #=[i**2 for i in suzulen] #Map ile
top= reduce(toplam,maplenen)

print liste,suzulen,maplenen,top

