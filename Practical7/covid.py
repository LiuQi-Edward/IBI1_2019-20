# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:54:23 2020

@author: bluem
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#1. import the .csv file
#specify to the right path of my computer
os.chdir("D:\刘其\大学学习\大一\IBI\Week 7. Public Health Informatics\Practical 7. Working with Global Health Data")
#use pandas to create a datafeame object
covid_data=pd.read_csv("full_data.csv")

#2. show all rows, and every third column between (and including) 0 and 15?
print(covid_data.iloc[0:18:3,:])

#3. use a Boolean to show "total cases" for all rows corresponding to Afghanistan
#first define a function to find the certain place to create a corresponding boolean variable of it
def find_loc(loc):
    boolean_loc=[]
    for i in covid_data.iloc[:,1]:
        if i==loc:
            boolean_loc.append(True)
        else:
            boolean_loc.append(False)
    return boolean_loc
#use the boolean-generating finction to find "Afghanistan" cases. Put it in the row argument.
Afghanistan_total_cases=covid_data.loc[find_loc("Afghanistan"),"total_cases"]

#4. use np to compute the mean and median of new cases for the entire world
world_new_cases=covid_data.loc[find_loc("World"),"new_cases"]
world_new_cases_np=np.array(world_new_cases[:])
world_new_cases_mean=np.mean(world_new_cases_np)
world_new_cases_median=np.median(world_new_cases_np)
print('\nworldwide mean',world_new_cases_mean)
print('worldwide median',world_new_cases_median)
      
#5. a boxplot of new cases worldwide
world_new_cases_boxplot=plt.boxplot(world_new_cases_np,
                                    vert=True,
                                    whis=1.5,
                                    patch_artist=True,
                                    showmeans=True,
                                    meanline=True,
                                    showbox=True,
                                    showcaps=True,
                                    showfliers=True,
                                    notch=False)
plt.ylabel('world_new_cases')
plt.title("New cases around the World")
plt.show()

#6. both new cases and new deaths worldwide
world_dates=covid_data.loc[find_loc("World"),"date"]
plt.plot(world_dates,
         world_new_cases,
         'r+')
world_new_deaths=covid_data.loc[find_loc('World'),'new_deaths']
plt.plot(world_dates,
         world_new_deaths,
         'b+')
plt.xlabel("dates")
plt.ylabel("world_new_cases")
plt.xticks(world_dates.iloc[0::4],rotation=-90)
plt.legend(['world_new_cases','world_new_deaths'])
plt.title("New cases and new deaths worldwide")
plt.show()

#7. question:How have new cases and total cases developed over time in Spain?
spain_dates=covid_data.loc[find_loc("Spain"),'date']
spain_total_cases=covid_data.loc[find_loc('Spain'),'total_cases']
spain_new_cases=covid_data.loc[find_loc('Spain'),'new_cases']
plt.plot(spain_dates,
         spain_new_cases,
         'r+')
plt.xlabel("dates")
plt.ylabel("spain_new_cases")
plt.xticks(spain_dates.iloc[0::4],rotation=-90)
#for plt.legend().do not write plt.legend("spain_new_cases").it will not show the complete legend.
plt.legend(["spain_new_cases"])
plt.title("Spain new cases developing")
plt.show()
#seperately show the two plots, because they are not in the same scale.
plt.plot(spain_dates,
         spain_total_cases,
         'b+')
plt.xlabel("dates")
plt.ylabel("spain_total_cases")
plt.xticks(spain_dates.iloc[0::4],rotation=-90)
plt.legend(["spain_total_cases"])
plt.title("Spain total cases developing")
plt.show()
