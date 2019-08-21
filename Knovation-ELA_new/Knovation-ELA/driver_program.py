# -*- coding: utf-8 -*-
"""
Knovation Resource Alignment
"""

#Importing modules
from Loading_Data import data_loading
from Data_Cleaning import basic_resource_data_cleaning,basic_standards_data_cleaning,making_nested_list_resource,making_nested_list_standards
from doc2vec import creatingTags,createGensimModels
from SimilarityMatrix3 import createSimilarityMatrix2
from Recommendation import recommendingResources
from output import resourceAlignmentOutput
import pandas as pd
from pickle import load
from sys import getsizeof
def processResourceAlignment(prop,log):
    # ------------------------------------------------------------------------------------------------------------------
    
    log.info("---------Into the driver program---------------")
    resources,standards = data_loading(prop,log)
    log.info("Before Cleaning Resources------"+str(len(resources)))
    log.info("Before Cleaning Standards------"+str(len(standards)))
    resources = basic_resource_data_cleaning(resources)
    standards = basic_standards_data_cleaning(standards)
    log.info("After Cleaning Resources-------"+str(len(resources)))
    log.info("After Cleaning Standards-------"+str(len(standards)))
    resources_length = len(resources)
    standards_length = len(standards)
    """
    combinedResource = making_nested_list_resource(resources)
    combinedStandards = making_nested_list_standards(standards)
    #Creating Corpus
    corpus = combinedResource+combinedStandards
    tags = creatingTags(corpus)
    createGensimModels(tags,prop)
    """
    #dataset = createSimilarityMatrix(prop)
    createSimilarityMatrix2(prop,standards,resources,standards_length,resources_length)
    #recommendedOutput = recommendingResources(prop,resources,standards,dataset)
    #resourceAlignmentOutput(prop,recommendedOutput)
    #print(recommendedOutput.shape)
   
    
