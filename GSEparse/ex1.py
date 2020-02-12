import sys
import gzip
import pandas as pd

b = 3
a = b+1
#df = pd.DataFrame({})
df = pd.read_csv('ex'+str(b)+'.tsv', sep='\t', header=0)
for i in range(10,15):
	#n = 0
	#f = gzip.open('./geoData2/'+str(i[0])+'_family.soft.gz','rt', encoding='utf-8', errors='ignore') 
	df.loc[i,'num'] = i	
	
df.to_csv("ex"+str(a)+".tsv",sep="\t",index=False,mode='a')

