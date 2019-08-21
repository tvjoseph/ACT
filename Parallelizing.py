# 7-July-2019

from multiprocessing import Process, Manager
import time

'''
References

https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba




'''

from pickle import load
from pickle import dump
from numpy.random import shuffle
# Saving a list of clean sentences to file
def save_clean_data(file,filename):
    dump(file,open(filename,'wb'))
    print('Saved: %s' % filename)
 # Loading the clean dataset
def load_clean_sentences(filename):
    return load(open(filename,'rb'))

	
Vecdf = load_clean_sentences('D:/Knovation_proj/vec_df.pkl')
#print(Vecdf.shape)

resourceDf = Vecdf[:47035,:]
#print(resourceDf.shape)
# Taking the standard data frame

standDf = Vecdf[47035:,:]
#print(standDf.shape)

from gensim import matutils
from numpy import dot


def cosine_dot(d1,d2,return_dict,i):
    return_dict[i] = dot(matutils.unitvec(d1), matutils.unitvec(d2))
    #print(i)
    #print(return_dict.values())
    return return_dict 

import multiprocessing

d1 = standDf[0]

#print('Start the multiprocessing')
	
if __name__ == '__main__':
    starttime = time.time()
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    for i in range(500):
        d2 = resourceDf[i]
        p = multiprocessing.Process(target=cosine_dot, args=(d1,d2,return_dict,i))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
		
    return_dict = dict(return_dict)
		
    	
    #print(return_dict.values(),return_dict.keys())
		
    save_clean_data(return_dict,'D:/Knovation_proj/return_dict.pkl')
        
    print('That took {} seconds'.format(time.time() - starttime))
	
