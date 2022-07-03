#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

filter/map örneği
"""



liste=["Python", "Ruby", "pHp", "jAVA", "scala","go"]

def suz(x):
    return x.istitle()  #Büyük harfle başlıyorsa dönder



def cevir(x):
    return x.capitalize() #İlk harfi büyük harfe çevirip dönder


print filter(suz,liste)
print map(cevir,liste)