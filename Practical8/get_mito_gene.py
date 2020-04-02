# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:59:25 2020

@author: bluem
"""
#import the re module
import re
#open the file in read mode
s=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#create to write the target file
newfile=open('mito_gene.fa',"w")
#convert the file content to a single string
f=s.read()
#find all information of mitochondria gene
seq_mito=re.findall(r'>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?>',f)
#create a new list
l1=[]
#manipulate each gene as a string in seq_mito
for gene in seq_mito:
#delete the unnecessary part
    simplify_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
#delete the '\n' and '>'
    newone=simplify_seq_mito.replace('>','').replace('\n','')
#calculate the gene length
    length=len(newone)-11
#add the gene length inforamtion to the gene information string
    a=">"+'gene length:'+str(length)+' '+newone+"\n"
#save the mature(simplified) gene information in the list
    l1.append(a)
#write the mature(simplified) in the newfile
    newfile.write(a)
#close the file
newfile.close()
#check whether the newfile is written correctly
print(open('mito_gene.fa').read())
    
