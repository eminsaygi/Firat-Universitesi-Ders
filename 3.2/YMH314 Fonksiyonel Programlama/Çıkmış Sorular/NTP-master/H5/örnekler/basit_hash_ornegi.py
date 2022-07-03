#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

s stringi her harfi +1 harfle şifrelemek ve şifre çözmek
"""


ham="python programlama dili ile programlama yapmak python dilinde web2py ve django web frameworkleri mevcuttur"

sifrelenmis=""

harfler=" abcdefghijklmnopqrstuvwxyz "

for k in ham:
    if k in harfler:
        sifrelenmis+=harfler[harfler.index(k)+1]
        
cozulen=" "



for k in sifrelenmis:
    if k in harfler:
        cozulen+=harfler[harfler.index(k)-1]

print "\n", sifrelenmis
print "\n",cozulen