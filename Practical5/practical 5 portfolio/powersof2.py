# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:22:46 2020

@author: bluem
"""

#first input a positive number
a=eval(input("please input a positive integer, whcih is smaller than 8192\na= "))
#We will change the value of a in the follwing part. Therefore, the value of a should be stored in another variable.
b=a
#define a variable which can finally show the final result string
result=""
#a should be smaller than 8192. We begin trying from 2^13.
j=13
#begin trying by gradually subtracting j value 
while a!=0:
#if 2**j is smaller than a.We should subtract 2**j from a and focus on the remained part.
    if 2**j<=a:
        a-=2**j
#once we finish a try, we should add the calculating outcome to the result.
        if a!=0:
            result+="2**"+str(j)+"+"
#To avoid a "+" existing at the end of the expression formula. We should consider this special circumstance.
        else:
            result+="2**"+str(j)
#After one try we diminish j to prepare for another try.
        j-=1
    else:
        j-=1
#finally output the outcome
print(str(b)+" is "+result)


#This remind me of the Euclidean Algorithm, whcih can also solves this problem.
"""
x=eval(input("please input a positive integer x="))
print("{} is ".format(x),end="")
j=0
while x!=0:
    a=x%2
    x=(x-a)/2
    if a==1:
        if j==0:
            print("2**0",end="")
        else:
            print("+2**{}".format(j),end="")
    j+=1
"""  
    
    
    
    
    
