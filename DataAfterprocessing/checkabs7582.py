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
df = pd.read_csv("./geofinal/geo2mesh75_82000.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in range(3837,20000):
	#i = int(i[0].replace("GSE",""))
	tabs = str(df['ABSTRACT'].iloc[i])
	iabs = ""
		#df.loc[i,'ABSTRACT'] = line.replace(fseries,"").replace("\n","")
	pid = df['PubMed_ID'].iloc[i]
	response = urlopen(base+"efetch.fcgi?db="+db+"&id="+str(pid)+"&retmode="+retmode).readlines()
		#print(response)
		#response = json.loads(response.decode('utf-8'))
		#line = response.readlines()
	for s in response:
		s = str(s)
			#print(s)
		if fabs in s:
			check = True
				#print("fab"+s)
			iabs = iabs+ s.replace(fabs,"").replace("\\n'","").replace("b'","")
		elif check:
				#print("check"+s)
			iabs = iabs + s.replace("\\n'","").replace("b'","")
			if fend in s:
				check = False
				iabs = iabs + s.replace(fend,"").replace("\\n'","").replace("b'","")
				#break
	print(i)
	df.loc[i,'ABSTRACT'] = iabs.strip()		
	df.to_csv("./geofinal/geo2mesh75_8200checked2.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

