#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

04242370001-1001 şeklinde verilen bir telefon numarası formatını
0424 2370001 1001 şeklinde split etme 
"""

tel="04242370001-1001"

no,dahili=tel.split("-")

alanadi, numara=no[0:4],no[4:]


print alanadi, numara,dahili


#join örneği
yeni=[alanadi,numara,dahili]

s=':'.join(yeni)
print s