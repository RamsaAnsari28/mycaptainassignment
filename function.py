# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:58:16 2022

@author: Khalid Ayub Ansari
"""

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] =1
        else:
            d[key] +=1
    return d
print('mississippi')
