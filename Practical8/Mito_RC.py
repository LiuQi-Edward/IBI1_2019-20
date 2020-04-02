# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:44:29 2020

@author: bluem
"""

filename=input("Please input a file name:")
compl_mito=open(filename,'w')
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

import re
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
f=a.read()
seq_mito=re.findall(r'>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?>',f)
l1=[]
for gene in seq_mito:
#delete the unnecessary part
    simplify_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
#delete the '\n' and '>'
    newone=simplify_seq_mito.replace('>','').replace('\n','')
    length=len(newone)-11
    a=">"+'gene length:'+str(length)+' '+newone+"\n"
    l1.append(a)
l2=[]
for g in l1:
    c=compl_cvt(''.join(re.findall(r'([ACGT]+)',g)))
    g2=re.sub(r'[ACGT]+',c,g)
    compl_mito.write(g2)
    l2.append(g2)
compl_mito.close()
    
    
