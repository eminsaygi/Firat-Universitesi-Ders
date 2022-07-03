#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr
Dosya ve klasörleri listelemek
"""

import os


print os.getcwd()
print os.chdir('/')  #Kök dizine geç
print os.getcwd()

for i in os.listdir(os.getcwd()):
    if os.path.isfile(i): 
        print "Dosya=>",i
    else:
        print "Klasor=>",i
