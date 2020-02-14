from fuzzywuzzy import process
import pandas as pd
import time
import csv

#data_me=pd.read_csv('/content/drive/My Drive/intern/me.csv', sep='\t')
data_me =pd.read_csv('../../Downloads/sum.csv', sep='\t')['GSE_SUMMARY'].values.tolist()
df =pd.read_csv('../../Downloads/sum.csv', sep='\t')
mydict = dict(zip(df.GSE_SUMMARY, df.GSE))
#data_sum=pd.concat([data_me, data_you], ignore_index=True)

syn = pd.read_csv("../final/synonym.tsv", sep='\t')['synonym'].values.tolist()
syndf = pd.read_csv("../final/synonym.tsv", sep='\t')
syndict = dict(zip(syndf.synonym, syndf.id))
# data_sum=pd.DataFrame(data_sum[['GSE_SUMMARY','GSE']])
# name_new=pd.DataFrame(name[['id','synonym']])
# name_sy=name_new.loc[40000:50000].reset_index()

def get_matches(query, choices):
  results = process.extract(query, choices, limit=20000)
  return results

for k in range(110000,130000):
  matches = get_matches(syn[k],data_me)
  num = 0
  for i in matches:
    if(i[1] >=60):
      print(mydict[i[0]])
      num = num +1
      f = open("./nlp_me_71_5.tsv", "a")
      writer = csv.writer(f, delimiter='\t')
      print(syndict[syn[k]]+" "+ mydict[i[0]]+ " "+str(i[1]) +" "+ syn[k]+' S')
      writer.writerow((syndict[syn[k]], mydict[i[0]], syn[k], i[1] ,'S'))
