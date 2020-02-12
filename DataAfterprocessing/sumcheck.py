import sys
import gzip
import pandas as pd
from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys

db ='pubmed'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
retmode = 'html'
nd = pd.read_csv('./nd.tsv', sep='\t').values.tolist()
#content = f.read()
#print(ucon)
#ln = len(ucon.readlines())
#print(ln)
check = False
fabs = "abstract \""
fend = ".\","
df = pd.read_csv("./geofinal/final/geo2mesh32checked2_ff.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in range(0,20000):
	#i = int(i[0].replace("GSE",""))
	tabs = str(df['GSE_SUMMARY'].iloc[i]).strip()
	df.loc[i,'GSE_SUMMARY'] = tabs		
	df.to_csv("./geofinal/geo2mesh32checked2_fff.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

