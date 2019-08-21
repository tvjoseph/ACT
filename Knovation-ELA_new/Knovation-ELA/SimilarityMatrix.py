# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:03:13 2019

@author: subramaniam.sethu
"""

from gensim.models.doc2vec import Doc2Vec
from gensim import matutils
from numpy import dot
import numpy as np
import pandas as pd
import _pickle as cpickle
#from pickle import dump
#from numpy.random import shuffle


def createSimilarityMatrix(prop):
    
    fname = (prop.get("Filepaths", "Model_Saving_Path"))
    model = Doc2Vec.load(fname)
    # Making the vectors of the documents

    vec_df = model.docvecs.vectors_docs
    print(vec_df.shape)
    #vec_df
    # Let us now seperate the resources matrix and also the standards matrix
    resourceDf = vec_df[:46116,:]
    print(resourceDf.shape)
    # Taking the standard data frame
    
    standDf = vec_df[46116:,:]
    print(standDf.shape)
    def cosine_dot(d1,d2):
        return dot(matutils.unitvec(d1), matutils.unitvec(d2))
    simMat2 = np.zeros((12307,46116))
    for i in range(len(standDf)):
        print(i)
        d2 = standDf[i]
        for j in range(len(resourceDf)):
            d1 = resourceDf[j]
            simMat2[i,j] = cosine_dot(d1,d2)
    simMat = pd.DataFrame(simMat2)
    del simMat2
    print("Executed successfully")
    #print(simMat.shape)
    #simMatlist = np.array_split(simMat,3)
    # Saving a list of clean sentences to file
    def save_clean_data(file,filename):
        cpickle.dump(file,open(filename,'wb'))
        print('Saved: %s' % filename)
    # Saving the similarity matrix in the folder
    #for i in range(len(simMatlist)):
    #	save_clean_data(simMatlist[i],(prop.get("Filepaths", "Model_Saving_Path")+"simMat.pkl"+str(i+1)+".pkl"))
    save_clean_data(simMat,(prop.get("Filepaths", "Model_Saving_Path")+"simMat.pkl"))
    return simMat