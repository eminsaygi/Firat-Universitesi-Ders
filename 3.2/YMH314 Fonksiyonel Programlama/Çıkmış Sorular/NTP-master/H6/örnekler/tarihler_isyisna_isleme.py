#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:42:32 2018

@author: sntr

sys.exit ve eval kullanımına örnek
"""


import datetime


def valid(yil,ay,gun):
    try:
        tarih=datetime.date(yil,ay,gun)
        return tarih
    except ValueError:
        return False


tarih1=valid(2018,13,34)
tarih2=valid(2018,03,18)

print tarih1
print tarih2