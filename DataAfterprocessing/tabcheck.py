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
df = pd.read_csv("./geofinal/final/geo2mesh3200checked2_ff_2.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in range(0,20000):
	#i = int(i[0].replace("GSE",""))
	tabs = str(df['GSE_SUMMARY'].iloc[i])
	iabs = ""
	#print(tabs)
	if "\n" in tabs:
		tabs = tabs.replace("\t","")
		tabs = tabs.strip()
		print("5"+tabs)	
	if "\t" in tabs:
		tabs = tabs.replace("\t","")
		tabs = tabs.strip()
		print("1"+tabs)
		#break
	if "    " in tabs:
		tabs = tabs.replace("    ","")
		tabs = tabs.strip()
		print("4"+tabs)
	if "   " in tabs:
		tabs = tabs.replace("   ","")
		tabs = tabs.strip()
		print("2"+tabs)
	if "  " in tabs:
		tabs = tabs.replace("  ","")
		tabs = tabs.strip()
		print("3"+tabs)
	else :
		continue
	
#	print(i)
	df.loc[i,'GSE_SUMMARY'] = tabs		
	df.to_csv("./geofinal/final/geo2mesh3200checked2_ff_2.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

