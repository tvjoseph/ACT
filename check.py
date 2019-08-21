from gensim.models.doc2vec import Doc2Vec
import numpy as np
fname = ('/home/SubramaniamS/Knovation-ELA/Model/model_July12_doc2vec_ELA.bin')
model = Doc2Vec.load(fname)
# Making the vectors of the documents

vec_df = model.docvecs.vectors_docs
#vec_df
# Let us now seperate the resources matrix and also the standards matrix
resourceDf = vec_df[:46116,:]
print(resourceDf.shape)
# Taking the standard data frame
    
standDf = vec_df[46116:,:]
print(standDf.shape)

for i in range(4):
    resourceDf = np.concatenate((resourceDf,resourceDf))
adding_resource = resourceDf[:300000,:]
resourceDf = np.concatenate((resourceDf,adding_resource))
print(resourceDf.shape)
sample_standards = standDf[:1000,:]
print(sample_standards.shape)
def normalise(A):
    lengths = (A**2).sum(axis=1, keepdims=True)**.5
    return A/lengths
ResourceDf = normalise(resourceDf)
sample_standards = normalise(sample_standards)
final = np.dot(sample_standards,ResourceDf.T)
print(final.shape)