#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:45:58 2018

@author: sntr
"""

class Faktoriyel():
    
    @staticmethod
    def f(n):
        return 1 if n==0 else n*Faktoriyel.f(n-1)
    


print Faktoriyel.f(5)
        