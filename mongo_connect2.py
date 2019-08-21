import pymongo
import pandas as pd	
client = pymongo.MongoClient("mongodb://ssethu:Gyt*R3^h@10.235.220.241:24017/alignment") # defaults to port 27017

db = client['alignment']

# print the number of documents in a collection
#print db.cool_collection.count()
print(db.list_collection_names())
collection = db['reviews']

cursor = collection.find({})
column_names = []
column_names.append('Standard GUID')
for i in range(1,101):
   column_names.append('Recommendation_'+str(i))
   column_names.append('Recommendation_'+str(i)+'_Similarity_Score')
#print(column_names)
resultant_df = pd.DataFrame(columns=column_names)
#print(resultant_df)
count=0
second_count = 1
for document in cursor:
   if second_count%1000==0:
     output_list=[]
     for i in document:
        if i!='_id':
           output_list.append(i)
           for j in document[i]:
              for k in j:
                  output_list.append(k)
                  output_list.append(str(round(float(j[k]),3)))
     print(second_count)  
     resultant_df.loc[count]=output_list
     count+=1

   second_count+=1
print(resultant_df)
resultant_df['Scores_Range'] = resultant_df['Recommendation_1_Similarity_Score']+'-'+resultant_df['Recommendation_100_Similarity_Score']
column_names.insert(1,'Scores_Range')
resultant_df = resultant_df[column_names]
resultant_df.to_csv('/home/SubramaniamS/SampleResult.csv',index=False)