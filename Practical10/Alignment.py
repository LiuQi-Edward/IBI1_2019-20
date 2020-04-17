# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:18:44 2020

@author: bluem
"""
#please run the programme with the existence of BLOSUM62 matrix.csv in your folder

#import necessary module re
import re
import pandas as pd
#read the file and extract the sequence as strings
file_name1=input("please input the first fasta file name:")
file_name2=input("please input the second fasta file name:")
file1=open(file_name1).read()
file2=open(file_name2).read()
#convert the list to a string
seq1=''.join(re.findall(r">.+?\n([A-Z]+)",file1))
seq2=''.join(re.findall(r">.+?\n([A-Z]+)",file2))

#calculate the hamming distance
edit_distance=0 #set initial distance as zero
for i in range(len(seq1)): #compare each amino acid
    if seq1[i]!=seq2[i]:
        edit_distance+=1 #add a score 1 if amino acids are different
print('\nthe hammning distance of two sequence is {}\n'.format(edit_distance))

"""
blosum62 source:
https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt

i use the website above to download the .txt file and i use str.repleace('  ',",") 
and str.repleace(',,',",") to change it into .csv format
"""

#read the "BLOSUM62 matrix.csv" as a dataframe
blosum62=pd.read_csv("BLOSUM62 matrix.csv")

"""
in the dataframe, the name of amino acid is in column-0,
we should define a function to correspond the amin oacid name to the row number
"""

#check each amino acid name one by one
def find_row_num(aa):
    j=0
    while True:
        if blosum62.iloc[j,0]!=aa:
            j+=1
        if blosum62.iloc[j,0]==aa:
            break
    return j

#calculate the blosum score
score=0
alignment=''
for i in range(len(seq1)):
    aa1=seq1[i]
    aa2=seq2[i]
#retrieve the score by giving 2 amino acid names
    score_plus=blosum62.loc[find_row_num(aa2),aa1]#use my function to find the corresponding amino acid row number
#acumulate the score
    score+=score_plus
    if aa1==aa2:
        alignment+=aa1
    elif score_plus>=0:
        alignment+='+'
    else:
        alignment+=" "
        
#print out the result
print('the bolusum62 score is {}\n'.format(score))
print("seq1:{}".format(seq1))
print("     {}".format(alignment))
print("seq2:{}".format(seq2))
    
    