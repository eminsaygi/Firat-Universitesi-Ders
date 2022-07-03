#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 22:36:08 2018

@author: sntr
"""
import httplib
conn = httplib.HTTPSConnection("www.milliyet.com.tr",timeout=0.1)
conn.request("GET", "/")
res = conn.getresponse()
print res.status, res.reason     

#print res.read()

#print res.msg