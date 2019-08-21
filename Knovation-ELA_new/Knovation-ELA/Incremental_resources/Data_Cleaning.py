# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:16:41 2019

@author: harini.sampathu
"""

# -*- coding: utf-8 -*-


import re
from nltk.corpus import stopwords

def basic_resource_data_cleaning(resource):
    resource = resource[~(resource["Eval Description"].isna())]
    resource = resource[~(resource["Eval Title"].isna())]
    resource = resource[~(resource["Keywords"].isna())]
    resource = resource[~(resource["Subject Node Lineage"].isna())]
    resource = resource[~(resource["Grade Levels"].isna())]
    print(len(resource))
    for i in range(0,len(resource)):
#        resource['Unnamed: 7'].iloc[i] = ' '.join(list(map(lambda x : 'Grade' + ' ' + x ,resource.iloc[i]['Grade Levels'].split('|'))))
        resource.loc[resource.index[i],'Únnamed: 7'] = ' '.join(list(map(lambda x : 'Grade' + ' ' + x ,resource.iloc[i]['Grade Levels'].split('|'))))
    resource = resource.rename(index=str,columns={'Unnamed: 7':'Grade'})
    # Let us now try to clean up the Keywords
    for i in range(0,len(resource)):
        docsplit = set(resource['Keywords'].iloc[i].split('|'))
        mylist = []
        for d in docsplit:
            mylist.append(d)
        seclist = ' '.join(mylist)
        newlist = seclist.split('\\')
        seclist = ' '.join(newlist)
#        resource['Unnamed: 8'].iloc[i] = [re.sub("[^a-zA-Z]", " ", seclist)][0]
        resource.loc[resource.index[i],'Unnamed: 8']  = [re.sub("[^a-zA-Z]", " ", seclist)][0]
    resource = resource.rename(index=str,columns={'Unnamed: 8':'Clean Keywords'})
    return resource


def basic_standards_data_cleaning(standards):
    print(standards.columns)
    standards = standards[~(standards["Standard Description"].isna())]
    standards = standards[~(standards["Standard Node Lineage"].isna())]
    return standards

def making_nested_list_resource(resource):
    def doc_to_words( raw_data ):
    #letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = raw_data.lower().split()                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))

    def doc_to_words2( raw_data ):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split('\\')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    
    def doc_to_words3( raw_data ):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split('|')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    def doc_to_words4( raw_data ):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split('>')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    def doc_to_words5( raw_data ):
        #letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = raw_data.lower().split('>')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    resdata1 = resource["Eval Description"]
    resdata2 = resource["Subject Node"]
    resdata3 = resource["Clean Keywords"]
    resdata4 = resource["Subject Node Lineage"]
    resdata5 = resource["Grade Levels"]
    
    clean_train_resdata1 = []
    clean_train_resdata2 = []
    clean_train_resdata3 = []
    clean_train_resdata4 = []
    clean_train_resdata5 = []
    
    for i in range( 0, len(resdata1) ):
        clean_train_resdata1.append( doc_to_words2( resdata1.iloc[i] ) )
        clean_train_resdata2.append( doc_to_words3( resdata2.iloc[i] ) )
        clean_train_resdata3.append( doc_to_words( resdata3.iloc[i] ) )
        clean_train_resdata4.append( doc_to_words4( resdata4.iloc[i] ) )
        clean_train_resdata5.append( doc_to_words( resdata5.iloc[i] ) )
        
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


def making_nested_list_standards(standards):
    def doc_to_words2( raw_data ):
        letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = letters_only.lower().split('\\')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    def doc_to_words5( raw_data ):
        #letters_only = re.sub("[^a-zA-Z]", " ", raw_data) 
        words = raw_data.lower().split('>')                             
        stops = set(stopwords.words("english"))                  
        meaningful_words = [w for w in words if not w in stops]   
        return( " ".join(meaningful_words ))
    stddata1 = standards["Standard Description"]
    stddata2 = standards["Standard Node Lineage"]
    clean_train_stddata1 = []
    clean_train_stddata2 = []

    for i in range( 0, len(stddata1) ):
        clean_train_stddata1.append( doc_to_words2( stddata1.iloc[i] ) )
        clean_train_stddata2.append( doc_to_words5( stddata2.iloc[i] ) )
    combStddata = list(zip(clean_train_stddata1, clean_train_stddata2))

    # Combinig both the strings for resources
    Stddata = []
    for i, _d in enumerate(combStddata):
        Stddata.append(_d[0] +' ' + _d[1]) 
    return Stddata
