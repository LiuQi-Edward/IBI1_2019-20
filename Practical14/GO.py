# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:39:48 2020

@author: bluem
"""
#import the necessary libraries
import xml.dom.minidom
import pandas as pd
#read the "go_obo.xml" in dom file
DOMTree=xml.dom.minidom.parse("go_obo.xml")
#extract the root node
root=DOMTree.documentElement
#make a list of term nodes
terms=root.getElementsByTagName("term")
#make some lists to store the extracted information. then use them to creat a dictionary. then creat a dataframe
id_list=[]
name_list=[]
definition_string_list=[]
childnode_list=[]
#define a function to calculate the childnodes
#the key in this function is the variable counter
def find(gene):
    find_list=[]
#make the variable 'counter' global so that during recursion, it will not back to zero
    global counter
    for term2 in terms:#loop each term to find the childnodes
        t2_is_a_list=term2.getElementsByTagName("is_a")
        #find all has <is_a> terms
        if t2_is_a_list!=[]:
            for t2 in t2_is_a_list:#find the specific childnodes
                if t2.childNodes[0].data==gene:
                    find_list.append(term2.getElementsByTagName('id')[0].childNodes[0].data)
                    counter+=1#add the counter by 1
    if find_list!=[]:#if the childnodes have their childnodes
        for id_element in find_list:
            find(id_element)#recurse to find child's childnodes
    return#return empty

#start retrieval and add the term with "autophagosome" in defstr into the list to finally create a dataframe
for term in terms:
    go_id=term.getElementsByTagName('id')[0]#id
    name=term.getElementsByTagName('name')[0]#name
    go_def=term.getElementsByTagName('def')[0]#def retrieval for defstr
    defstr=go_def.getElementsByTagName('defstr')[0]#defstr
    if "autophagosome" in defstr.childNodes[0].data:#judge whether it has "autophagosome"
        #if yes, add the data into the corresponding lists
        id_list.append(go_id.childNodes[0].data)
        name_list.append(name.childNodes[0].data)
        definition_string_list.append(defstr.childNodes[0].data)
        #set the initial counter value
        counter=0
        #invoke the function to calculate the childnodes
        find(go_id.childNodes[0].data)
        childnode_list.append(counter)
#create a dataframe
sum_dict={"id":id_list,"name":name_list,"definition string":definition_string_list,"childnodes":childnode_list}
sum_df=pd.DataFrame(sum_dict)
sum_df.to_excel("beginning of the autophagosome.xlsx")




