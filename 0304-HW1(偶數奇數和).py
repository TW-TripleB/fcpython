# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:37:10 2021

@author: user
"""
Sum=0
total=0
for i in range(1,51):
    if i%2==0:
        Sum+=i
    else:
        total+=i
        
print("偶數和:",Sum)
print("奇數和:",total)
