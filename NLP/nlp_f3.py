from fuzzywuzzy import fuzz
import pandas as pd
import time

#data_me=pd.read_csv('/content/drive/My Drive/minjj/me.csv', sep='\t')
#data_you=pd.read_csv('/content/drive/My Drive/minjj/you.txt', sep='\t')
data_sum=pd.read_csv('../../Downloads/sum.csv', sep='\t')

name=pd.read_csv('../final/synonym.tsv', sep='\t')

data_sum=pd.DataFrame(data_sum[['GSE_SUMMARY','GSE']])
name_new=pd.DataFrame(name[['id','synonym']])

print(data_sum[data_sum.duplicated()==True].count())
data_sum=data_sum.drop_duplicates(subset='GSE').reset_index()
data_sum[data_sum.duplicated()==True].count()

name_sy=name_new.loc[75220:79999].reset_index()
import csv
import time
startTime= time.time()


find=pd.DataFrame()
df=pd.DataFrame()
for i in range(len(name_sy)) :
  str1=name_sy.loc[i,'synonym']
    
  for j in range(len(data_sum)) :
    str2=data_sum.loc[j, 'GSE_SUMMARY']
    Token_set_Ratio = fuzz.token_set_ratio(str1, str2)
    if Token_set_Ratio > 60 :
      f = open("./nlp_me_71_5.tsv", "a")
      writer = csv.writer(f, delimiter='\t')
      #print(name_sy.loc[i, 'id']+ " "+ data_sum.loc[j, 'GSE'] +" " +name_sy.loc[i,'synonym']+" "+ Token_set_Ratio+' S')
      writer.writerow((name_sy.loc[i, 'id'], data_sum.loc[j, 'GSE'], name_sy.loc[i,'synonym'], Token_set_Ratio ,'S'))
      #print(df)
    else :
        continue
  print(i)
  
# find=df
# find.to_csv('/content/drive/My Drive/nlp_me_71_4.tsv', sep='\t')

endTime = time.time() - startTime
print(endTime)



