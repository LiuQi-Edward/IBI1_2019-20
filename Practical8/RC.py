# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:22:22 2020

@author: bluem
"""
seq='ATGCGACTACGATCGAGGGCCAT'
def compl_cvt(seq):
    compl_seq=""#create an empty string
    for b in seq[:]:
#judge each nucleotide base and convert it by adding them to the empty string from the end one by one.
        if b=="A":
            compl_seq="T"+compl_seq
        elif b=="T":
            compl_seq="A"+compl_seq
        elif b=="C":
            compl_seq="G"+compl_seq
        elif b=="G":
            compl_seq="C"+compl_seq
        else:#if the user mis-type the sqeuence, remind the user an undefined base
            print("undefined base","{}".format(b))
            break#jump out from the loop
    return compl_seq#return the complementary sequence
#use theself-defined function to convert the sequence
reverse_compl_seq=compl_cvt(seq)
#print the outcome
print("the reverse complementary sequence is {}".format(reverse_compl_seq))
