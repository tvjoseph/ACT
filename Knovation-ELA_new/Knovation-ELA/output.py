# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:03:03 2019

@author: subramaniam.sethu
"""


def resourceAlignmentOutput(prop,resMat):
    resMat.to_csv(prop.get("Filepaths", "Model_Saving_Path")+'output2.csv')
    