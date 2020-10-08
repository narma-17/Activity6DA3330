# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:55:31 2020

@author: User
"""

def simpsons(x,y):
    h=x[1]-x[0]
    n=len(y)-1
    s=0
    for i in range(n+1):#calculating area of each trapezoid of height h
        if i==0 or i==n:#sn=y0+yn
            s+=y[i]
        elif i%2 ==1:# +4*y_odd
            s+=4*y[i]
        else:
            s+=2*y[i]# +2*y_even
    s=s*h/3# *h/3 
    print (s)
    return s

#Driver Code
pt=[3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6]
t=[1,2,3,4,5,6,7,8,9]
integral=simpsons(t,pt)






