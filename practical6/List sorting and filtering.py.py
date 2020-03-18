# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:06:17 2020

@author: bluem
"""
#List sorting and filtering

#import module "matplotlib" and "numpy"
import matplotlib.pyplot as plt
#define a gene lenghth list
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#sort to rank the element in the list from the smallest to the largest
gene_lengths.sort()
#show the original gene list to the user
print("the original gene list: ",gene_lengths)
#remove the smallest one(first one)
del(gene_lengths[0])
#remove the largest one(the last one)
del(gene_lengths[-1])
#show the sorted gene list
print("sorted gene list: ",gene_lengths)
#prepare to draw a bar plot
#the number of y value
score=gene_lengths
#define a boxplot
plt.boxplot(score,#add the statistic length
            vert=True,#make the boxplot vertical
            whis=1.5,#Specifies the distance between the upper and lower quartiles.
            patch_artist=True,#fill the box with color
            meanline=False,#do not show the meanline. it will tangle up with median line
            showbox=True,#show the box
            showcaps=True,#show the line bottom and top line
            showfliers=True,#show abnoraml value
            notch=False,#no notch
            labels=["gene length distribution"]#add a label
            )
#show the boxplot
plt.show()




