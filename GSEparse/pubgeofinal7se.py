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
from urllib.error import HTTPError

db ='pubmed'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
retmode = 'xml'
nd = pd.read_csv('/home/meongeun/meshGeo/nd.tsv', sep='\t').values.tolist()
#content = f.read()
#print(ucon)
#ln = len(ucon.readlines())
#print(ln)

ftitle = "!Series_title = "
fseries = "^SERIES = "
fpubmed = "!Series_pubmed_id = "
fsum = "!Series_summary = "
ftype = "!Series_type = "
fsamid = "!Series_sample_id = "
fstax = "!Series_sample_taxid = "
fptax = "!Series_platform_taxid = "
fplatid = "!Series_platform_id = "
#b = 3
#a = b+1
#df = pd.read_csv("geo2mesh9.tsv", sep='\t',header=0)
df = pd.DataFrame({ 'GSE_SUMMARY':[['GSM117232','GSM117447']], 'GSM':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in nd[79921:82000]:
	n = 0
	f = gzip.open('/home/meongeun/meshGeo/geoData2/'+str(i[0])+'_family.soft.gz','rt', encoding='utf-8', errors='ignore') 
	samples = ""
	summary = ""
	i = int(i[0].replace("GSE",""))
	for line in f.readlines():
		if fseries in line:
			df.loc[i,'GSE'] = line.replace(fseries,"").replace("\n","")
		elif ftitle in line:
			df.loc[i,'GSE_TITLE'] = line.replace(ftitle,"").replace("\n","")
			#print(line)
		elif fpubmed in line:
			pid = line.replace(fpubmed,"").replace("\n","").replace(" ","")
			df.loc[i,'PubMed_ID'] = pid
		elif fsum in line:
			summary += line.replace(fsum,"").replace("\n","")
		elif ftype in line:
			df.loc[i,'DATA_TYPE'] = line.replace(ftype,"").replace("\n","")
		elif fsamid in line:
			n=n+1
			line = line.replace(fsamid,"").replace("\n","")
			samples += line+";"
		elif fplatid in line:
			df.loc[i,'Platform_ID'] = line.replace(fplatid,"").replace("\n","")
		elif fptax in line:
			df.loc[i,'Platform_TAX'] = line.replace(fptax,"").replace("\n","")
		elif fstax in line:
			df.loc[i,'Sample_TAX'] = line.replace(fstax,"").replace("\n","")
	df.at[i,'GSM'] = samples
	df.at[i,'GSE_SUMMARY'] = summary
	df.loc[i,'SAMPLES_N'] = n
	print(i)	
	df.to_csv("/home/meongeun/meshGeo/geo2mesh8/geo2mesh8_25.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

