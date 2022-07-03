#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:31:18 2018

@author: sntr
"""
class benzerlik():
    def __init__(self):
        self.liste=["ali","ahmet","karpuz","mehmet","python","ruby"]
    
    def bul(self,aranan):
        max=0
        benzeri=self.liste[0]
        for i in self.liste:
    
            toplam=0
            for j in aranan:
                toplam+=i.count(j)
                if toplam>max:
                    max=toplam
                    benzeri=i
        print aranan,"=>",benzeri
        
        

x=benzerlik()
x.bul("memet")
