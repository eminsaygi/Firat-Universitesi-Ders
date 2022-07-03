#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr
Belirli dosyaları listelemek ve ayrıntı elde etmek
"""
import os
for i in os.listdir(os.getcwd()):
    if i.endswith('.py'):
        print(i)
        
#os.rename("untitled1.py","deneme1.py") #Dosya ismini değiştirmek
        
        
print "Dosya ayrıntıları \n"
print os.stat("deneme1.py") #Dosya ayrıntıları
