import sys
import gzip
import pandas as pd

f = gzip.open('./geoData2/GSE5205_family.soft.gz','rb')
ln = len(f.readlines())
#print(ln)
n=0
fstring = "!Series_title"
df = pd.DataFrame({})
for line in f.readlines():
	if fstring in line:
		n+=1
		df['GSE_TITLE'] = line
		print(line)
	else: 
		n +=1




