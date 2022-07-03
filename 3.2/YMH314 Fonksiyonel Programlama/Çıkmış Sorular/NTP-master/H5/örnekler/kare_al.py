# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:44:34 2018

@author: FeyzaÖzbay
"""
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)