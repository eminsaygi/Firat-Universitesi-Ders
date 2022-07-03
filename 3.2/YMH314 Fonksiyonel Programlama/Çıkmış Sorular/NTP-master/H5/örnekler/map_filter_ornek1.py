#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:38:36 2018

@author: sntr

filter => (Süz) Gelen parametre True ise dönder 
map    => (Değiştir) Gelen parametre üzerinde değişiklik yaparak dönderir

"""

x=range(100)

def suzgec(x):
    return x%5==0 #5'e bölünüyorsa dönder


def degis(x):
    return x*2+1  #Gelen sayının 2.katının 1 fazlasını dönder


print "Filtre örneği",filter(suzgec,x)
print "\n"
print "Map örneği",map(degis,x)
