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


nr = pd.read_csv('./nr.tsv', sep='\t').values.tolist()
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
#df = pd.read_csv("geo2mesh2.tsv",delimiter='\t')
df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in nr[2927:]:
	n = 0
	f = gzip.open('./geoData2/'+str(i[0])+'_family.soft.gz','rt', encoding='utf-8', errors='ignore') 
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
		#print(abstract)
			#print(i)
			#df.loc[i,'PubMed_ID'] = pid 
			df.loc[i,'TITLE'] = title
			df.loc[i,'ARTICLE_TITLE'] = art_title
			df.loc[i,'ABSTRACT'] = abstract
			df.loc[i,'GSE_DISEASE_TERM'] = mesh
			#df.to_csv("pub2mesh.tsv",mode='a', header=False, index=False, sep="\t")	
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
	df.to_csv("geo2mesh3.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

