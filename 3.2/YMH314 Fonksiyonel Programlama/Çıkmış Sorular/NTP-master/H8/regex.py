#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:01:56 2018

@author: sntr
"""

import re

ptrn="^\d{1,2}\/\d{1,2}\/\d{4}$"
t="12/03/2018"

a= re.match(ptrn,t)

if a:
    print "ok"
else:
    print "yok"