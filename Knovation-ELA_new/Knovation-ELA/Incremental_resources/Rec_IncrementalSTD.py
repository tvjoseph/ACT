# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:08:36 2019

@author: jennifer.john
"""

from gensim.models.doc2vec import Doc2Vec
from gensim import matutils
from numpy import dot
import numpy as np
import pandas as pd
from pickle import dump
import pymongo
from pymongo import MongoClient
#from numpy.random import shuffle


def createSimilarityMatrix2(prop,New_Std_vector,resources,standards_length,resources_length,New_standard_data):
    client = MongoClient(port=27017) # defaults to port 27017
    db = client['Alignment']
    
    fname = (prop.get("Filepaths", "Model_Saving_Path"))
    model = Doc2Vec.load(fname)
    # Making the vectors of the documents

    vec_df = model.docvecs.vectors_docs
    vec_df.shape
    #vec_df
    # Let us now seperate the resources matrix and also the standards matrix
    resourceDf = vec_df[:resources_length,:]
    print("Printing the type of ResourceDF")
    print(type(resourceDf))
    # Taking the standard data frame
    
    standDf = New_Std_vector
    print("Printing the type of StandDF")
    print(type(standDf))

    def cosine_dot(d1,d2):
        return dot(matutils.unitvec(d1), matutils.unitvec(d2))

    #print(resourceDf[0])
    #print(standDf[0])
    print("Printed the first element of res and std")
    #simMat2 = np.zeros((standards_length,resources_length))
    for i in range(standards_length):
        simMat2 = np.zeros((1,resources_length))
        d2 = standDf[i]
        print(type(d2))
        print(d2)

        for j in range(len(resourceDf)):
            d1 = resourceDf[j]
            print(d1)
            print(type(d1))

            simMat2[0,j] = cosine_dot(d1,d2)
        simMat = pd.DataFrame(simMat2)
        print("Sim mat to pd df")
        
        std1 = simMat.loc[0].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:100]
        std2 = simMat.loc[0].sort_values(ascending=False, kind='quicksort',na_position='last')[0:100]
        scores_list = std2.tolist()
        print(len(scores_list))
       
        contents = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade Levels']]
        result={}
        result[str(New_standard_data.iloc[i]['GUID'])] = []
        count = 0
        for j in range(2,len(contents)*3,3):
            result2 = {}
            m = int((j-2)/3)
            result2[str(contents.iloc[m]['Eval Code'])] = str(scores_list[count])
            result[str(New_standard_data.iloc[i]['GUID'])].append(result2)
            count+=1
            #result[str(standards.iloc[i]['GUID'])].append(str(contents.iloc[m]['Eval Code']))
        print(result)
        print("********"+str(i))
        result1 = db.New_Standards_recommendation .insert(result,check_keys=False)
