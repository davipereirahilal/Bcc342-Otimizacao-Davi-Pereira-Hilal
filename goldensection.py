# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kUO4BPrhpaXyrD7djX9ZAgh00nkJj8mo
"""

import math
gr = (math.sqrt(5) + 1) / 2

def goldensection(f, a, b, t=0.0005):
 c = b - (b - a) / gr
 d = a + (b - a) / gr
 while (b - a) > t:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr

 return (b + a) / 2


f= lambda x:(x+2)**2
b= goldensection(f,2,6)
print( b)