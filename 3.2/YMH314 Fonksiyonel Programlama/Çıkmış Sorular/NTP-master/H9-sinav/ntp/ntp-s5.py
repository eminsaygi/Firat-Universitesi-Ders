#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:51:19 2018

@author: sntr
"""

import os


print os.getcwd()
#print os.chdir('/')  #Kök dizine geç
print "dizin",os.getcwd()

if not os.path.exists('./yedekler'):
    os.mkdir('yedekler')       


try:
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i): 
            dosya_adi, uzanti = os.path.splitext(i) 
            print uzanti
            if uzanti=='.txt':
                print "var"
                os.rename(i,'./yedekler/'+dosya_adi+".txt")   
        

except Exception, e:
    print "Hata",str(e)

finally:
    print "son"
                
                
