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
retmode = 'xml'
nd = pd.read_csv('./nd.tsv', sep='\t').values.tolist()
#content = f.read()
#print(ucon)
#ln = len(ucon.readlines())
#print(ln)
check = False
fabs = "abstract \""
fend = ".\","
df = pd.read_csv("geo2mesh7.tsv", sep='\t',header=0)
#df = pd.DataFrame({'GSM':[['GSM117232','GSM117447']], 'GSE_SUMMARY':[['GSM117232','GSM117447']]})
#print(f.read())
#print(type(nr[0]))
for i in range(0,12000):
	#i = int(i[0].replace("GSE",""))
	tabs = str(df['PubMed_ID'].iloc[i])
	iabs = ""
	if tabs:
		#df.loc[i,'ABSTRACT'] = line.replace(fseries,"").replace("\n","")
		pid = df['PubMed_ID'].iloc[i]
		try:
			response = urlopen(base+"efetch.fcgi?db="+db+"&id="+str(pid)+"&retmode="+retmode).read()
		except HTTPError as e:
			content = e.read()
		#print(pid)
		xtree = ET.fromstring(response)
		abstract = ""
		mesh = ""
		title = xtree.find("PubmedArticle/MedlineCitation/Article/Journal/Title").text
		art_title = xtree.find("PubmedArticle/MedlineCitation/Article/ArticleTitle").text
		if(xtree.find("PubmedArticle/MedlineCitation/Article/Abstract")):
			for j in xtree.find("PubmedArticle/MedlineCitation/Article/Abstract"):
				if j.text is None:
					abstract = 'error'
				else:
					abstract += j.text
				
				#print(j.text)
				#print(xtree.find("PubmedArticle/MedlineCitation/Article/Abstract").text)
		if(xtree.find("PubmedArticle/MedlineCitation/MeshHeadingList")):
			for j in xtree.find("PubmedArticle/MedlineCitation/MeshHeadingList"):
				#print(j)
				mesh += j.find("DescriptorName").text+","
				for k in j.findall("QualifierName"):
					#print(n)
					mesh += k.text+","
			#print(abstract)
			#print(i)
			#df.loc[i,'PubMed_ID'] = pid 
		df.loc[i,'TITLE'] = title
		df.loc[i,'ARTICLE_TITLE'] = art_title
		df.loc[i,'ABSTRACT'] = abstract
		df.loc[i,'GSE_DISEASE_TERM'] = mesh
		#print(response)
		#response = json.loads(response.decode('utf-8'))
		#line = response.readlines()
		
	else :
		continue
	print(i)
		
	df.to_csv("geo2pub9.tsv",sep="\t", index=False)
#if fsamid in content:
#	df.loc[i,'GSM'] = content.replace(fsamid,"")
#		print(no)
#
#print(samples)
#print(df)

