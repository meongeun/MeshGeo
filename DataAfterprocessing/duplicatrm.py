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

#nd = pd.read_csv('./nd.tsv', sep='\t').values.tolist()
df = pd.read_csv("/home/meongeun/meshGeo/geofinal/geo2mesh32000.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
df.drop_duplicates(['GSE'], keep='first')
df.to_csv("./geofinal/geo2mesh32000_du.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

