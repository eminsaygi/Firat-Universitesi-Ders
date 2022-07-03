#!/usr/bin/python

dict = {'Isim': 'Zara', 'Yas': 7, 'Sinif': 'First'}
print dict
dict['Yas'] = 8; # update existing entry
dict['Okul'] = "DPS School"; # Add new entry
 

print "dict['Yas']: ", dict['Yas']
print "dict['Okul']: ", dict['Okul']
print dict
del dict['Isim']; #remove entry with key 'Name'
print dict