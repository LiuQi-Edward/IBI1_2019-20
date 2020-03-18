# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:40:21 2020

@author: bluem
"""

#Counting DNA nucleotides

#import the matplotlib.pyplot module and keyboard module
import matplotlib.pyplot as plt
#let the user input the DNA sequence
sequence=input("please input a sequence of DNA(e.g.ATCGGATA...):")
#count the number of each nucleotide in the sequence
a=sequence.count("A")#count 'A'
g=sequence.count("G")#count 'G'
c=sequence.count("C")#count 'C'
t=sequence.count("T")#count 'T'       
#create sunch a dictionary
dictionary={"A":a,"G":g,"C":c,"T":t}
print("the frequency dictionary is:\n {}".format(dictionary))
#prepare to create the pie plot
labels="A","G","C","T"#add labels
sizes=[a,g,c,t]#fill in the values
explode=(0,0,0,0)#I do not want to emphasize anyone. Therefore, let none of them stand out.
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.2f%%",shadow=False,startangle=90)
#ensure the pie is a circle
plt.axis("equal")
#show the pie plot
plt.show