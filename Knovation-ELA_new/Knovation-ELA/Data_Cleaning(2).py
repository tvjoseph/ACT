33# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:06:28 2019

@author: subramaniam.sethu
"""

import re
from nltk.corpus import stopwords

def basic_resource_data_cleaning(resource,prop):
    column_names = prop.get("Resource_Columns","Column_Names")
    column_names = column_names.split(',')
    for i in column_names:
        resource = resource[~(resource[i].isna())]

    for i in range(0,len(resource)):
        resource['Unnamed: 7'].iloc[i] = ' '.join(list(map(lambda x : 'Grade' + ' ' + x ,resource.iloc[i]['Grade Levels'].split('|'))))
    resource = resource.rename(index=str,columns={'Unnamed: 7':'Grade'})
    # Let us now try to clean up the Keywords
    print("******")
    for i in range(0,len(resource)):
        docsplit = set(resource['Keywords'].iloc[i].split('|'))
        mylist = []
        for d in docsplit:
            mylist.append(d)
        seclist = ' '.join(mylist)
        newlist = seclist.split('\\')
        seclist = ' '.join(newlist)
        resource['Unnamed: 8'].iloc[i] = [re.sub("[^a-zA-Z]", " ", seclist)][0]
        print(i)
    print("******")
    resource = resource.rename(index=str,columns={'Unnamed: 8':'Clean Keywords'})
    return resource


def basic_standards_data_cleaning(standards,prop):
    print(standards.columns)
    column_names = prop.get("Standard_Columns","Column_Names")
    column_names = column_names.split(',')
    for i in column_names:
        standards = standards[~(standards[i].isna())]
    return standards

def making_nested_list_resource(resource,prop):
    def doc_to_words(raw_data,string):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split(string)                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    column_names = prop.get("Resource_Columns","Column_Names")
    column_names = column_names.split(',')
    result= {}
    for i in range(len(column_names)):
        result['resdata'+str(i)] = resource[i]
    
    clean_train_resdata1 = []
    clean_train_resdata2 = []
    clean_train_resdata3 = []
    clean_train_resdata4 = []
    clean_train_resdata5 = []
    
    for i in range( 0, len(result["resdata"+str(1)]) ):
        clean_train_resdata1.append( doc_to_words(result['resdata'+str(i)].iloc[i]),prop.get("Resource_Cleaning", "Delimiter_"+str(i)) )
        
    print(len(clean_train_resdata1))    
    print(len(clean_train_resdata2))
    print(len(clean_train_resdata3))
    print(len(clean_train_resdata4))
    print(len(clean_train_resdata5))
    combResdata = list(zip(clean_train_resdata1,clean_train_resdata3,clean_train_resdata4, clean_train_resdata5)) # ,clean_train_resdata3, clean_train_resdata2
    print(len(combResdata))

    # Combinig both the strings for resources
    Resdata = []
    for i, _d in enumerate(combResdata):
        Resdata.append(_d[0] +' ' + _d[1]+' ' + _d[2]+' ' + _d[3]) 
    
    return Resdata


def making_nested_list_standards(standards,prop):
    def doc_to_words2( raw_data,string ):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split(string)                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    column_names = prop.get("Standard_Columns","Column_Names")
    column_names = column_names.split(',')
    result= {}
    for i in range(len(column_names)):
        result['stddata'+str(i)] = standards[i]
    clean_train_stddata1 = []
    clean_train_stddata2 = []

    for i in range( 0, len('stddata'+str(1)) ):
        clean_train_stddata1.append( doc_to_words2(result['stddata'+str(i)].iloc[i]),prop.get("Standard_Cleaning", "Delimiter_"+str(i)) )
    combStddata = list(zip(clean_train_stddata1, clean_train_stddata2))

    # Combinig both the strings for resources
    Stddata = []
    for i, _d in enumerate(combStddata):
        Stddata.append(_d[0] +' ' + _d[1]) 
    return Stddata
