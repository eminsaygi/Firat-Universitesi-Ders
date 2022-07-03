#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
nums = [x for x in range(10)]
random.shuffle(nums)
print nums
t=sum(nums)
print t
nums.sort()
print "Sayilar"
for j in nums:
    print j
kontrol=True
for i in range(2,t-1):
    if t%i==0:
        kontrol=False
        print t," rastgele sayilarin toplami asal degildir"
        break
if kontrol:
    print t," rastgele sayilarin toplamý asaldýr"