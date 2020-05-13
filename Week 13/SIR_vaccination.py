# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:58:30 2020

@author: bluem
"""

#import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
#define a function to delete all the specified identical elements(e) in a list(l)
def del_all(l,e):
    while e in l:
        l.remove(e)
    return l
#define the percentage of vaccinated ones
pv=0
#add pv by 0.1 increments
while pv<1.1:
    N=10000
    S=9999
    I=1
    R=0
    V=pv*N
#i include the vaccinated people in the Recoverd herd
    R+=V
#recalculate the susceptible ones
    S=int(N-I-R)
    beta=0.3
    gamma=0.05
    R_track=[R]
    S_track=[S]
    I_track=[I]
    for i in range(1,1000):
#infrctious rate
        p=beta*(I/N)
#choose S numbers in a list containing 0 or 1 (0-susceptible, 1-infected) 
        choose_S=list(np.random.choice(range(2),S,p=[1-p,p]))
#use my function to delete all 0 in the list and calculate the 1 numbers(infected numbers-S change)
        S_change=len(del_all(choose_S,0))
        S-=S_change
        I=I+S_change
#use the same method to calculate the recoverd ones
        choose_R=list(np.random.choice(range(2),I,p=[1-gamma,gamma]))
        R_change=len(del_all(choose_R,0))
        R+=R_change
        I=I-R_change
        R_track.append(R)
        S_track.append(S)
        I_track.append(I)
    plt.plot(list(range(1000)),I_track,color=cm.viridis(50+500*pv),marker = ',',linestyle = '-',label = '{:.1f}'.format(pv))
    plt.legend()
    pv+=0.1        

plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of infected people')
plt.show()


