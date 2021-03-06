# -*- coding: utf-8 -*-
"""descidagradiente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m1nJ3B6DbeLsM9lEeRfast2Nx3YxK4D9
"""

from os import name
import numpy as np
import math

def interpolacaoquadratica(f,a,b,tol=1e-6):
  c = b
  b = (c-a)/2

  fa = f(a)
  fb = f(b)
  fc = f(c)

  while abs(c-a) < tol:
    x = 0.5*(fa*(b**2-c**2)+fb*(c**2-a**2)+fc*(a**2-b**2))/(fa*(b-c) +fb*(c-a) +fc*(a-b))
    fx = f(x)
    print(x)
    if x > b:
      if fx > fb:
        c = x
        fc = fx
      else: 
        a = b
        fa = fb
        b = x
        fb = fx
    else:
      if fx > fb:
        a = x
        fa = fx
      else:
        c = b
        fc = fb
        b = x
        fb = fx

  return (a+c)/2

def bracketing(a,f,s=0.01,m=2):
    b = a + s

    fa=f(a)
    fb=f(b)
    if fa > fb :
        c=b+s
        fc=f(c)
        while fc < fb :
                fb=fc
                b=c
                s=s*m
                c=c+s
                fc=f(c)
        bracketing =[a,c]
        
    
    if fb > fa:
            a=b-s
            c=a-s
            fc=f(c)
            while fc < fa :
            
                    fa=fc
                    a=c
                    s=s*m
                    c=c-s
                    fc=f(c)
                    
            bracketing = [c,b]

    return bracketing

def  descidagradiente(x,f,grad,tol=1e-6,alpha=[],inter=interpolacaoquadratica):

  lx = [x]
  lfx = [f(x)]

  got_alpha = True if alpha else False 

  gradx = grad(x)

  while np.linalg.norm(gradx) > tol:

    if not got_alpha:
      f_aux = lambda a : f(x - a*gradx)
      bracket = bracketing(0,f_aux)
      alpha = inter(f_aux,bracket[0],bracket[1],tol=tol)
      
    x = x - alpha*gradx
    gradx = grad(x)

    lx.append(x)
    lfx.append(f(x))

  return x,f(x),lx,lfx