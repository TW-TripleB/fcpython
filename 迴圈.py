# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:48:31 2021

@author: user
"""
'''
print(list(range(10)))
print(list(range(0,9)))
print(list(range(1,10,2)))
print(list(range(10,1,-1)))
'''

for i in range(1,10):
    if i%2==0:
        print(i,"是偶數")
    else:
        print(i,"是奇數")
print("finish")    

