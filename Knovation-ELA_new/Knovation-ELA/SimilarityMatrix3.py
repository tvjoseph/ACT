# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:49:38 2019

@author: subramaniam.sethu
"""


from gensim.models.doc2vec import Doc2Vec
from gensim import matutils
from numpy import dot
import numpy as np
import pandas as pd
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
    batch_count = int(prop.get("Standard_Batches", "Batch_Count"))
    quotient_count = len(standDf)/batch_count
    reminder_count = len(standDf)%batch_count
    for i in range(int(quotient_count)):
        d2 = standDf[i*batch_count:(i+1)*batch_count,:]
        def normalise(A):
            lengths = (A**2).sum(axis=1, keepdims=True)**.5
            return A/lengths
        d1 = resourceDf
        ResourceDf = normalise(d1)
        d2 = normalise(d2)
        final = np.dot(d2,ResourceDf.T)
        print(final.shape)
        simMat = pd.DataFrame(final)
        for j in range(0,batch_count):
            print(j)
            std1 = simMat.loc[j].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:100]
            std2 = simMat.loc[j].sort_values(ascending=False, kind='quicksort',na_position='last')[0:100]
            scores_list = std2.tolist()
            #print(len(scores_list))
            contents = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade']]
            result={}
            result[str(standards.iloc[(i*batch_count)+j]['GUID'])] = []
            count = 0
            for k in range(2,len(contents)*3,3):
                result2 = {}
                m = int((k-2)/3)
                result2[str(contents.iloc[m]['Eval Code'])] = str(scores_list[count])
                result[str(standards.iloc[(i*batch_count)+j]['GUID'])].append(result2)
                count+=1
    
            #result1 = db.reviews.insert_one(result)
           
        #For Remaining Standards

        d2 = standDf[i*batch_count:(i*batch_count)+reminder_count,:]
        def normalise(A):
            lengths = (A**2).sum(axis=1, keepdims=True)**.5
            return A/lengths
        d1 = resourceDf
        ResourceDf = normalise(d1)
        d2 = normalise(d2)
        final = np.dot(d2,ResourceDf.T)
        print(final.shape)
        simMat = pd.DataFrame(final)
        for j in range(i*batch_count,(i*batch_count)+reminder_count):
            print(j)
            std1 = simMat.loc[j].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:100]
            std2 = simMat.loc[j].sort_values(ascending=False, kind='quicksort',na_position='last')[0:100]
            scores_list = std2.tolist()
            #print(len(scores_list))
            contents = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade']]
            result={}
            result[str(standards.iloc[(i*batch_count)+j]['GUID'])] = []
            count = 0
            for k in range(2,len(contents)*3,3):
                result2 = {}
                m = int((k-2)/3)
                result2[str(contents.iloc[m]['Eval Code'])] = str(scores_list[count])
                result[str(standards.iloc[(i*batch_count)+j]['GUID'])].append(result2)
                count+=1
                #result[str(standards.iloc[(i*batch_count)+j]['GUID'])].append(str(contents.iloc[m]['Eval Code']))
    
            #result1 = db.reviews.insert_one(result)

