#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr

sys kullanarak konsoldan girilen argümanların toplanması

c:\> python konsoldan_toplama 1 3 5 gibi çalıştırılacak
"""


import sys

t=0
for i in range(1,len(sys.argv)):
    t+=int(sys.argv[i])


print t