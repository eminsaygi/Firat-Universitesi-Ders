#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:57:59 2018

@author: sntr
"""

import random
import string

class verigizle():
    def __init__(self,msj):
        self.msj=msj
        self.metin=(random.sample(string.letters,50)*len(msj))
        self.fibolustur()
        
    
    def fibolustur(self):
        self.fibs=[1,2]
        for i in range(2,len(self.msj)):
            self.fibs+=[self.fibs[i-1]+self.fibs[i-2]]
        print self.fibs
    
    
    def verigizle(self):
        for i in range(len(self.fibs)):
            self.metin[self.fibs[i]]=self.msj[i]
        return ''.join(self.metin)
        
    
    def vericoz(self,metin):
        msg=""
        for i in range(len(self.fibs)):
            msg+=metin[self.fibs[i]] 
        return ''.join(msg)


v=verigizle("Python del to")
print "Rastgele metin =>",''.join(v.metin)
gizlenen=v.verigizle()
print "Ham veri gizlenmiş metin =>",gizlenen
cozulen=v.vericoz(gizlenen)
print "Çözülen metin =>",cozulen

