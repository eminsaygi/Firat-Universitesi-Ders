#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:41:57 2018

@author: sntr
"""

class matris():
    def __init__(self,n):
        self.n=n
        self.matrisiolustur()
    
    def matrisiolustur(self):
        print [ [i*j if i==j else 0 for j in range(self.n)] for i in range(self.n)]
    



m=matris(5)