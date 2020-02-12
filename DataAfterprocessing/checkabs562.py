import sys
import gzip
import pandas as pd
import urllib, urllib3
from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys

db ='pubmed'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
retmode = 'html'
nd = pd.read_csv('/home/meongeun/meshGeo/nd.tsv', sep='\t').values.tolist()
#content = f.read()
#print(ucon)
#ln = len(ucon.readlines())
#print(ln)
check = False
fabs = "    abstract \""
fend1 = ".\","
fend2 = "mesh {"
df = pd.read_csv("/home/meongeun/meshGeo/geo2mesh562all.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in range(0,20000):
	#i = int(i[0].replace("GSE",""))
	tabs = str(df['ABSTRACT'].iloc[i])
	iabs = ""
		#df.loc[i,'ABSTRACT'] = line.replace(fseries,"").replace("\n","")
	pid = df['PubMed_ID'].iloc[i]
	pid = str(pid)
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=%s&retmode=html' % (pid)
	response = requests.get(base, params={'db':db, 'id':pid,'retmode':retmode})
	
		#response = json.loads(response.decode('utf-8'))
		#line = response.readlines()
	for s in response.iter_lines():
		s = str(s)
			#print(s)
		if fabs in s:
			check = True
				#print("fab"+s)
			iabs = iabs+ s.replace(fabs,"").replace("\\n'","").replace("b'","")
		elif check:
				#print("check"+s)
			iabs = iabs + s.replace("\\n'","").replace("b'","")
			if fend1 in s:
				check = False
				iabs = iabs + s.replace(fend1,"").replace("\\n'","").replace("b'","")
			if fend2 in s: 
				check = False
				iabs = iabs + s.replace(fend2,"").replace("\\n'","").replace(    "b'","")	
				#break
	print(i)
	df.loc[i,'ABSTRACT'] = iabs.replace('\t'," ").strip()		
	df.to_csv("/home/meongeun/meshGeo/geofinal/geo2mesh5_62000fchecked.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

