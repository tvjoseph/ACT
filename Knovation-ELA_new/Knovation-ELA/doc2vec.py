# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:07:01 2019

@author: subramaniam.sethu
"""

from gensim.models.doc2vec import TaggedDocument
import gensim.models as g
from nltk.tokenize import word_tokenize

def creatingTags(corpus):
    tagged_data = [TaggedDocument(words=word_tokenize(_d), tags=[str(i)]) for i, _d in enumerate(corpus)]
    return tagged_data

def createGensimModels(tags,prop):
    #doc2vec parameters
    vector_size = int(prop.get("doc2vec parameters", "vector_size"))
    window_size = int(prop.get("doc2vec parameters", "window_size"))
    min_count = int(prop.get("doc2vec parameters", "min_count"))
    sampling_threshold = float(prop.get("doc2vec parameters", "sampling_threshold"))
    negative_size = int(prop.get("doc2vec parameters", "negative_size"))
    train_epoch = int(prop.get("doc2vec parameters", "train_epoch"))
    dm = int(prop.get("doc2vec parameters", "dm")) #0 = dbow; 1 = dmpv
    worker_count = int(prop.get("doc2vec parameters", "worker_count"))  #number of parallel processes
    print("Into the function")
    #pretrained word embeddings
    pretrained_emb =  (prop.get("Filepaths", "Pretrained_Word_Embeddings"))
    print("Loaded the file")
    #input corpus
    #train_corpus = combDoc["Description"]
    
    #output model
    saved_path = (prop.get("Filepaths", "Model_Saving_Path"))
    
    #enable logging
    print("Creating Model")
    #train doc2vec model
    #docs = g.doc2vec.TaggedLineDocument(train_corpus)
    model = g.Doc2Vec(tags, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count, hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)
    print("Saving model")
    #save model
    model.save(saved_path)
    