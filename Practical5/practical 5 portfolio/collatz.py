# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:37:47 2020

@author: bluem
"""
#randomly input a positive interger as the initial value
n=eval(input("Please input a positive integer n="))
c=n
#keep calculating the value of c until c=1
while c!=1:
#if c is even
    if c%2==0:
#according to collatz sequence, c=c/2
        c=c/2
#show the c value
        print(c)
#if c is odd
    else:
#according to collatz sequence, c=3c+1
        c=3*c+1
#show the c value
        print(c)
    
