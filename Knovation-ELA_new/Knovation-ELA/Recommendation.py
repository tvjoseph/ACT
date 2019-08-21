# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:50:01 2019

@author: subramaniam.sethu
"""


from pickle import load
import random
import numpy as np
import pandas as pd

def recommendingResources(prop,resources,standards,dataset):
    # Loading the clean dataset
    #dataset = pd.read_csv('/home/SubramaniamS/output.csv',header=None,index=True)	
    def load_clean_sentences(filename):
        return load(open(filename,'rb'))
    #dataset = load_clean_sentences(prop.get("Filepaths", "Model_Saving_Path")+'simMat.pkl')
    def Reco(idx):    
        std1 = dataset.loc[idx].sort_values(ascending=False, kind='quicksort', na_position='last').index[0:15]
        content = resources.iloc[std1][['Eval Title','Eval Description','Subject Node','Eval Code','Grade']]
        return content

    stdRange = range(0, len(standards))
    #stdRange = random.sample(range(0, )

    resMat = np.zeros((len(standards),47)).astype(object)
    
    for i,std in enumerate(stdRange):
        contents = Reco(std)
        resMat[i,0] = standards.iloc[std]['Standard Title']
        resMat[i,1] = standards.iloc[std]['Standard Description']
        for j in range(2,len(contents)*3,3):
            k = j+1
            l = j + 2
            m = int((j-2)/3)
            resMat[i,j] = contents.iloc[m]['Eval Code']
            resMat[i,k] = contents.iloc[m]['Eval Title']
            resMat[i,l] = contents.iloc[m]['Eval Description']    
    resMat = pd.DataFrame(resMat)
    resMat.columns = ['Standard Title','Standard Desc','Reco1 Eval Code','Reco1 Eval Title','Reco1 Eval Desc','Reco2 Eval Code','Reco2 Eval Title','Reco2 Eval Desc','Reco3 Eval Code','Reco3 Eval Title','Reco3 Eval Desc','Reco4 Eval Code','Reco4 Eval Title','Reco4 Eval Desc','Reco5 Eval Code','Reco5 Eval Title','Reco5 Eval Desc','Reco6 Eval Code','Reco6 Eval Title','Reco6 Eval Desc','Reco7 Eval Code','Reco7 Eval Title','Reco7 Eval Desc','Reco8 Eval Code','Reco8 Eval Title','Reco8 Eval Desc','Reco9 Eval Code','Reco9 Eval Title','Reco9 Eval Desc','Reco10 Eval Code','Reco10 Eval Title','Reco10 Eval Desc','Reco11Eval Code','Reco11 Eval Title','Reco11 Eval Desc','Reco12 Eval Code','Reco12 Eval Title','Reco12 Eval Desc','Reco13 Eval Code','Reco13 Eval Title','Reco13 Eval Desc','Reco14 Eval Code','Reco14 Eval Title','Reco14 Eval Desc','Reco15 Eval Code','Reco15 Eval Title','Reco15 Eval Desc']
    return resMat