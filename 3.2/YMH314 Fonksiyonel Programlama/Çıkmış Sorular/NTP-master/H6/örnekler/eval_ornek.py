#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr

sys.exit ve eval kullanımına örnek
"""

import sys

while True:
    print "1.sayi="
    a=input()
    print "\n 2.sayi="
    b=input()
    
    print "islem: + - * / cikmak icin x :"
    op=raw_input()
    if op=='x':
        sys.exit()
    else:
        islem=str(a)+op+str(b)
        
        print "\nsonuc=",eval(islem)  #Eval python ortamında kod çalıştırır/işlem yapar