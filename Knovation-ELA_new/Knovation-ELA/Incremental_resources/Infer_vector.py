# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:47:30 2019

@author: harini.sampathu
"""
import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec


def Load_newData(prop,log):
    New_standards = pd.read_csv(prop.get("Filepaths", "New_Standard_Path"),encoding = "ISO-8859-1")
    return New_standards
    

def InferVector(prop,log,New_std_nested_list):
     Vec_df = np.zeros(shape=(len(New_std_nested_list),50))
     fname = (prop.get("Filepaths", "Model_Saving_Path"))
     model = Doc2Vec.load(fname)
     
     for i in range( 0, len(New_std_nested_list) ):
        #print(i)
        temp = New_std_nested_list[i]
        temp = str(temp)
        Vec_df[i] = model.infer_vector([temp])
     return Vec_df

