# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:18:07 2019

@author: harini.sampathu
"""

#Importing modules
from Loading_Data import data_loading
from Data_Cleaning import basic_resource_data_cleaning,basic_standards_data_cleaning,making_nested_list_resource,making_nested_list_standards
#from Infer_vector import Load_newData,InferVector
#from Infer_vecRes import Load_newData,InferVector

#from Similarity_NewStandard import createSimilarityMatrix_NewStandard
#from doc2vec import creatingTags,createGensimModels
#from Recommendation_NewSTD import recommendingResourcesForNewSTD,resourceAlignmentOutput
import sys
#import pandas as pd


#from Similarity_NewStandard import createSimilarityMatrix_NewStandard
#from doc2vec import creatingTags,createGensimModels
#from Recommendation_NewSTD import recommendingResourcesForNewSTD,resourceAlignmentOutput
#import numpy as np
#from pyMongo import createSimilarityMatrix_NewStandard
#from Rec_IncrementalSTD import createSimilarityMatrix2
"""

from SimilarityMatrix2 import createSimilarityMatrix2
from Recommendation import recommendingResources
from output import resourceAlignmentOutput
import pandas as pd
from pickle import load
from sys import getsizeof
"""
def processResourceAlignment(prop,log):
     #------------------------------------------------------------------------------------------------------------------
    if sys.argv[1]=='train':
        log.info("---------Into the driver program---------------")
        resources,standards = data_loading(prop,log)
        print(resources.columns)
        print(standards.columns)
        log.info("Before Cleaning Resources------"+str(len(resources)))
        log.info("Before Cleaning Standards------"+str(len(standards)))
        resources = basic_resource_data_cleaning(resources)
        standards = basic_standards_data_cleaning(standards)
        print(resources.info())
        print(standards.info())
        log.info("After Cleaning Resources-------"+str(len(resources)))
        log.info("After Cleaning Standards-------"+str(len(standards)))
        resources_length = len(resources)
        standards_length = len(standards)
        print(len(resources))
        print(len(standards))
    
        #combinedResource = making_nested_list_resource(resources)
        #print(type(combinedResource))
        #print(getsizeof(combinedResource))
        #combinedStandards = making_nested_list_standards(standards)
        #print(type(combinedStandards))
        #print(getsizeof(combinedStandards))
        #log.info(str(len(combinedResource)))
        #log.info(str(len(combinedStandards)))
        #log.info(combinedResource[0])
        #log.info(combinedStandards[0])
        #Creating Corpus
        #corpus = combinedResource+combinedStandards
        #print(type(corpus))
        #print(getsizeof(corpus))
        #tags = creatingTags(corpus)
        #print(type(tags))
        #print(getsizeof(tags))
        #createGensimModels(tags,prop)
        #dataset = createSimilarityMatrix(prop)
        #createSimilarityMatrix2(prop,standards,resources,standards_length,resources_length)
        #recommendedOutput = recommendingResources(prop,resources,standards,dataset)
        #resourceAlignmentOutput(prop,recommendedOutput)
        #print(recommendedOutput.shape)
        #data = pd.read_csv("/home/SubramaniamS/output.csv")
        #print(data.shape)
        #print(data.iloc[1])
    elif sys.argv[1]=='test':
        log.info("---------Into the driver program---------------")
        resources,standards = data_loading(prop,log)
        print(standards.columns)
        print(len(resources))
        print(len(standards))
        
                
        log.info("Before Cleaning Resources------"+str(len(resources)))
        log.info("Before Cleaning Standards------"+str(len(standards)))
        
        resources = basic_resource_data_cleaning(resources)
        standards = basic_standards_data_cleaning(standards)
        print("Basic cleaning done")
        
        """
        log.info("After Cleaning Standards-------"+str(len(standards)))
        
           
        standards_length = len(standards)
	resources_length = len(resources) 
        #print(len(resources))
        print("Res and std length stored")
        
        #For New Resources
        New_resources_data = Load_newData(prop,log)
        print(len(New_resources_data))
        print(New_resources_data.columns)
        
        New_resources_data = basic_resource_data_cleaning(New_resources_data)        
        New_res_nested_list = making_nested_list_resource(New_resources_data)
        
        print("New resources imported and cleaned")
        print(len(New_res_nested_list))
        
        New_Res_vector = InferVector(prop,log,New_res_nested_list)
        print("Printing the type of Res vec")
        print(type(New_Res_vector))
    
        createSimilarityMatrix2(prop,New_Res_vector,resources_length,standards_length)
	"""
        