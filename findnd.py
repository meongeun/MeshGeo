import sys
import pandas as pd

f = open('./gds_result1.txt','r')
#ln = len(f.readlines())
#print(ln)

fstring = "Series		Accession: "
df = pd.DataFrame({})
i=0
for line in f.readlines():
	if fstring in line:
		i=i+1
		item = line.replace(fstring,"").split("\t")
		df.loc[i,'AccessionNum'] = item[0]
		#print(item[0])
		#print(line.replace(fstring,"").replace("   ID:     200127893",""))
print("finish")
df.to_csv("nd.tsv",sep="\t", index=False)
		




