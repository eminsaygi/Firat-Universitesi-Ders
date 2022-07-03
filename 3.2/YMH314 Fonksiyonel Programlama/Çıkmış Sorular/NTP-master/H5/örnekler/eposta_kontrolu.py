#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:53:54 2018

@author: sntr

stringin işlemi kullanarak e-mail adresi geçerliliği kontrol etme
isim@alanadi.uzanti

@ ve . olmalı isim, alanadi ve uzanti en az 2 karakter uzunlukta olmalı
"""

def kontrol(s):
    if s.count("@")>0:
        isim,uzanti=s.split("@")
        if uzanti.count(".")>0:
            alanadi,uzanti=uzanti.split(".")
            if len(alanadi)>=2 and len(uzanti)>=2:
                return True
            else:
                return False
        else:
            return False
                
    else:
        return False
        

eposta1="ali@ali.com" #Geçerli
eposta2="ali_ali.com" #Geçerli Değil
eposta3="a@a.com" #Geçerli Değil


print kontrol(eposta1)
print kontrol(eposta2)
print kontrol(eposta3)

