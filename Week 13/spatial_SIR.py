# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:50:49 2020

@author: bluem
"""

import numpy as np
import matplotlib.pyplot as plt
#make an array of susceptible population
population=np.zeros((100,100))
#pick a random number for row
a=np.random.choice(range(100),1)
#pick a random number for column
b=np.random.choice(range(100),1)
#mutate a random person to become infected
population[a,b]=1
ok=np.where(population==0)
for i in range(100):
    if i==0:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    if i==9:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    if i==49:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    if i==99:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    beta=0.3
    gamma=0.05
# find infected points
    infectedIndex = np.where(population==1)
# loop through all infected points
    for i in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    #for an infected person, he/she has some probability to recover
        population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])



