#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:51:18 2018

@author: sntr
"""

import sqlite3 as sql
vt = sql.connect('deneme')
im = vt.cursor()
#im.execute("CREATE TABLE personel (isim, soyisim, memleket)")
im.execute("insert into personel values ('yunus', 'santur', 'Elz') ")

im.execute("update personel set memleket = 'Elazig' ")

im.execute("delete from personel where isim='yns' ")

rows=im.execute("select * from personel")

for k in rows:
    print k


vt.commit()
vt.close()
