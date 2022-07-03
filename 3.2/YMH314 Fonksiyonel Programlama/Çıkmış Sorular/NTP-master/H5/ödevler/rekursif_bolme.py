#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 23:01:17 2018

@author: sntr

Rekürsif float bölme 

"""

def bol(x,y,bolum=0,kalan=0,ondalik=0,s="",b=""):
    if x<y:
        x=x*10
        b=""
        for i in range(5):
	        while (x-y>=0):
	            x=x-y
	            ondalik+=1
       		b=b+str(ondalik) 
        return (x,y,bolum,kalan,ondalik,b)


    else:
        bolum+=1
        return bol(x-y,y,bolum,kalan,ondalik,s="",b="")
    

sonuc= bol(10,5)
s=str(sonuc[2])+"."+str(sonuc[5])
print "sonuc=",s
