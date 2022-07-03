# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:44:34 2018

@author: FeyzaÖzbay
"""
def cube(x): 
    return x*x*x
result=map(cube, range(1, 11))

numberscube = set(result)
print(numberscube)