from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys


db ='pubmed'
geo2mesh = pd.read_csv("geo2mesh.tsv", delimiter='\t')
geo2mesh = geo2mesh[geo2mesh!=0].dropna()
pmid = geo2mesh['PubMed_ID'].values.tolist()
#print(pmid)
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
retmode = 'xml'
df = pd.read_csv('pub2mesh.tsv', delimiter='\t',header=None)
#print(df)
#df = pd.DataFrame({'GSE_DISEASE_TERM':[[]]})
#print(abstract)
for i in pmid:
	response = urlopen(base+"efetch.fcgi?db="+db+"&id="+str(i)+"&retmode="+retmode).read()
	xtree = ET.fromstring(response)
	abstract = ""
	mesh = ""
	title = xtree.find("PubmedArticle/MedlineCitation/Article/Journal/Title").text
	art_title = xtree.find("PubmedArticle/MedlineCitation/Article/ArticleTitle").text
	for j in xtree.find("PubmedArticle/MedlineCitation/Article/Abstract"):
		abstract += j.text
	for j in xtree.find("PubmedArticle/MedlineCitation/MeshHeadingList"):
		#print(j)
		mesh += j.find("DescriptorName").text+","
		for n in j.findall("QualifierName"):
			#print(n)
			mesh += n.text+","
	#print(abstract)
	print(i)
	df.loc[i,'PubMed_ID'] = i
	df.loc[i,'TITLE'] = title
	df.loc[i,'ARTICLE_TITLE'] = art_title
	df.loc[i,'ABSTRACT'] = abstract
	df.loc[i,'GSE_DISEASE_TERM'] = mesh
	df.to_csv("pub2mesh.tsv",mode='a', header=False, index=False, sep="\t")
#print(xtree.find("Title"))	
#for i in xtree.find("IdList"):
#	print(i.text)
#row.append({"count":count, "idList":idList})
#df = pd.DataFrame(rows,columns = ["count","idList"])

#print(df)


