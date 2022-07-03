#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr

Zaman aritmetiği

"""

import datetime

bugun=datetime.datetime.today()

fark=datetime.timedelta(weeks=0,days=1,hours=0, minutes=0, seconds=0)

yarin=bugun+fark
dun=bugun-fark
ikigunoncesi=bugun-fark*2


print bugun
print yarin
print dun
print ikigunoncesi

print "dun bugünden küçükmü: ", dun<bugun


#formatı değişken olarak almak
format = "%a %b %d %H:%M:%S %Y"
print datetime.datetime.strftime(bugun,format)

