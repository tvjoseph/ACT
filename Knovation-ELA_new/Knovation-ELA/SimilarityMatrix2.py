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
    username = prop.get("MongoDB Credentials", "username")
    password = prop.get("MongoDB Credentials", "password")
    ip = prop.get("MongoDB Credentials", "ip")
    port = prop.get("MongoDB Credentials", "port")
    database_name = prop.get("MongoDB Credentials", "database_name")
    url = "mongodb://"+username+":"+password+"@"+ip+":"+port+"/"+database_name
    client = MongoClient(url)
    #client = MongoClient("mongodb://ssethu:Gyt*R3^h@10.235.220.241:24017/alignment") # defaults to port 27017
    db = client['alignment']
    
    fname = (prop.get("Filepaths", "Model_Saving_Path"))
    model = Doc2Vec.load(fname)
    # Making the vectors of the documents

    vec_df = model.docvecs.vectors_docs
    vec_df.shape
    #vec_df
    # Let us now seperate the resources matrix and also the standards matrix
    resourceDf = vec_df[:resources_length,:]
    print(resourceDf.shape)
    # Taking the standard data frame
    
    standDf = vec_df[resources_length:,:]
    print(standDf.shape)
    def cosine_dot(d1,d2):
        return dot(matutils.unitvec(d1), matutils.unitvec(d2))
    print(resourceDf[0])
    print(standDf[0])
    #simMat2 = np.zeros((standards_length,resources_length))
    for i in range(10000):
        simMat2 = np.zeros((1,resources_length))
        d2 = standDf[i]
        for j in range(len(resourceDf)):
            d1 = resourceDf[j]
            simMat2[0,j] = cosine_dot(d1,d2)
        simMat = pd.DataFrame(simMat2)
        std1 = simMat.loc[0].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:100]
        std2 = simMat.loc[0].sort_values(ascending=False, kind='quicksort',na_position='last')[0:100]
        scores_list = std2.tolist()
        #print(len(scores_list))
        contents = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade']]
        result={}
        result[str(standards.iloc[i]['GUID'])] = []
        count = 0
        for j in range(2,len(contents)*3,3):
            result2 = {}
            m = int((j-2)/3)
            result2[str(contents.iloc[m]['Eval Code'])] = str(scores_list[count])
            result[str(standards.iloc[i]['GUID'])].append(result2)
            count+=1
            #result[str(standards.iloc[i]['GUID'])].append(str(contents.iloc[m]['Eval Code']))
        #print(result)
        print("********"+str(i))
        #result1 = db.reviews.insert(result,check_keys=False)
        

