# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:58:30 2020

@author: bluem
"""

#import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt
N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05
R_track=[R]
S_track=[S]
I_track=[I]
def del_all(l,e):
    while e in l:
        l.remove(e)
    return l
for i in range(1,1000):
    p=beta*(I/N)
    choose_S=list(np.random.choice(range(2),S,p=[1-p,p]))
    S_change=len(del_all(choose_S,0))
    S-=S_change
    I=I+S_change
    choose_R=list(np.random.choice(range(2),I,p=[1-gamma,gamma]))
    R_change=len(del_all(choose_R,0))
    R+=R_change
    I=I-R_change
    R_track.append(R)
    S_track.append(S)
    I_track.append(I)
plt.plot(list(range(1000)),S_track,'r+',marker = ',',linestyle = '-',label = 'Susceptible')
plt.plot(list(range(1000)),I_track,'b+',marker = ',',linestyle = '-',label = 'Infected')
plt.plot(list(range(1000)),R_track,'g+',marker = ',',linestyle = '-',label = 'Recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()