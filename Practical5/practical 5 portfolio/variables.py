# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:30:18 2020

@author: bluem
"""
#4.1 Some simple math
print("4.1 Some simple math")
a=123
b=123123
c=b/7
d=c/11
e=d/13
print("a=123\n\n My input 'b' value is {}. After instructed calculation, e={}".format(b,e))
#4.2 Booleans
print("4.2 Booleans")
#Create a Booleans variable X 
X=eval(input("please input a Boolean variable X="))
#Create a Booleans variable Y
Y=eval(input("please input a Boolean variable Y="))
#Calculate the value of Z
Z=(X and (not Y))or(Y and (not X))
#In another way, calculate W, which should be the same value of W
W=X!=Y
#print Z and W to enable the user verify the consistence of Z and W
print("\nThe 'Z' value is {}\nThe 'W' value is {}".format(Z,W))
print("Whether Z=W?",Z==W)
