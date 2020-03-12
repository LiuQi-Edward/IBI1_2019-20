# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:08:18 2020

@author: bluem
"""

# What does this piece of code do?
# Answer: 
#To randomly draw a prime number from 1 to 100
# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)#draw a number from 1 to 100
    u = ceil(n**(0.5))
    for i in range(2,u+1):#to select the number that cannot be divided by any number except 1 and itself
        if n%i == 0:
            p=False


     
print(n)