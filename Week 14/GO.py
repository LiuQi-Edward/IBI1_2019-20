# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:39:48 2020

@author: bluem
"""
import xml.dom.minidom
import pandas as pd
DOMTree=xml.dom.minidom.parse("go_obo.xml")
root=DOMTree.documentElement
terms=root.getElementsByTagName("term")
id_list=[]
name_list=[]
definition_string_list=[]
childnode_list=[]
def find(gene):
    find_list=[]
    global counter
    for term2 in terms:
        t2_is_a_list=term2.getElementsByTagName("is_a")
        if t2_is_a_list!=[]:#
            for t2 in t2_is_a_list:
                if t2.childNodes[0].data==gene:
                    find_list.append(term2.getElementsByTagName('id')[0].childNodes[0].data)
                    counter+=1
    if find_list!=[]:
        for id_element in find_list:
            find(id_element)
    return
for term in terms:
    go_id=term.getElementsByTagName('id')[0]
    name=term.getElementsByTagName('name')[0]
    go_def=term.getElementsByTagName('def')[0]
    defstr=go_def.getElementsByTagName('defstr')[0]
    if "autophagosome" in defstr.childNodes[0].data:
        id_list.append(go_id.childNodes[0].data)
        name_list.append(name.childNodes[0].data)
        definition_string_list.append(defstr.childNodes[0].data)
        counter=0
        find(go_id.childNodes[0].data)
        childnode_list.append(counter)
sum_dict={"id":id_list,"name":name_list,"definition string":definition_string_list,"childnodes":childnode_list}
sum_df=pd.DataFrame(sum_dict)
sum_df.to_excel("beginning of the autophagosome.xlsx")




