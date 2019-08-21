# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:52:06 2019

@author: harini.sampathu
"""

import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec


def Load_newData(prop,log):
    New_resources = pd.read_csv(prop.get("Filepaths", "New_Resource_Path"),encoding = "ISO-8859-1")
    return New_resources
    

def InferVector(prop,log,New_res_nested_list):
     Vec_df = np.zeros(shape=(len(New_res_nested_list),50))
     fname = (prop.get("Filepaths", "Model_Saving_Path"))
     model = Doc2Vec.load(fname)
     
     for i in range( 0, len(New_res_nested_list) ):
        #print(i)
        temp = New_res_nested_list[i]
        temp = str(temp)
        Vec_df[i] = model.infer_vector([temp])
     return Vec_df

from pickle import dump
from pymongo import MongoClient
#from numpy.random import shuffle


def createSimilarityMatrix2(prop,standards,resources,standards_length,resources_length):
    client = MongoClient(port=27017)
    db=client.knovation
    
    fname = (prop.get("Filepaths", "Model_Saving_Path"))
    model = Doc2Vec.load(fname)
    # Making the vectors of the documents

    vec_df = model.docvecs.vectors_docs

    #vec_df
    # Let us now seperate the resources matrix and also the standards matrix
    resourceDf = vec_df[:resources_length,:]
    print(resourceDf.shape)
    # Taking the standard data frame
    
    standDf = vec_df[resources_length:,:]
    print(standDf.shape)
    del vec_df
    quotient_count = len(standDf)/10000
#    reminder_count = len(standDf)%10000
    for i in range(int(quotient_count)):
        d2 = standDf[i*10000:(i+1)*10000,:]
        def normalise(A):
            lengths = (A**2).sum(axis=1, keepdims=True)**.5
            return A/lengths
        d1 = resourceDf
        ResourceDf = normalise(d1)
        d2 = normalise(d2)
        final = np.dot(d2,ResourceDf.T)
        print(final.shape)
        simMat = pd.DataFrame(final)
        for j in range(0,10000):
            print(j)
            std1 = simMat.loc[j].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:100]
            std2 = simMat.loc[j].sort_values(ascending=False, kind='quicksort',na_position='last')[0:100]
            scores_list = std2.tolist()
            #print(len(scores_list))
            contents = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade']]
            result={}
            result[str(standards.iloc[(i*10000)+j]['GUID'])] = []
            count = 0
            for k in range(2,len(contents)*3,3):
                result2 = {}
                m = int((k-2)/3)
                result2[str(contents.iloc[m]['Eval Code'])] = str(scores_list[count])
                result[str(standards.iloc[(i*10000)+j]['GUID'])].append(result2)
                count+=1
                #result[str(standards.iloc[(i*10000)+j]['GUID'])].append(str(contents.iloc[m]['Eval Code']))
#            print(result)
            print((i*10000)+j)
    
            #result1 = db.reviews.insert_one(result)

    

    
    