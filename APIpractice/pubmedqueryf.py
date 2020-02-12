from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys

finall = pd.read_csv("./geofinal/final/final.tsv",sep='\t')
pubmedl = finall[['GSE','PubMed_ID']].values.tolist()
#print(pubmedl)
table = pd.DataFrame({'GSE':[''], 'PubMed_ID':[''],'MeshID':[['D0000','D9458245','D0098']],'D/S':['']})
syn = pd.read_csv("./geofinal/final/synonym.tsv", sep='\t')
s2d = set(syn['id'].values)
db ='pubmed'
#pmid = '28755519' 
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
#table['GSE'] = finall['GSE']
i = 1
for gse, pmid in pubmedl:
	print(gse, pmid)
	response = urlopen(base+"efetch.fcgi?db="+db+"&id="+str(pmid)+"&retmode=xml").read()
	xtree = ET.fromstring(response)
#print(xtree.find("MedlineCitation"))
	mesh = set()
	if(xtree.find("PubmedArticle/MedlineCitation/MeshHeadingList")):
		for j in xtree.find("PubmedArticle/MedlineCitation/MeshHeadingList"):                    #print(j)
			mesh.add(j.find("DescriptorName").get('UI'))
			for k in j.findall("QualifierName"):
				#print(n)
				mesh.add(k.get('UI'))
	exact = mesh & s2d
	table.loc[i, 'GSE'] = gse
	table.at[i, 'MeshID'] = list(exact)
	table.loc[i, 'PubMed'] = pmid
	table.loc[i, 'D/S'] = "D"
	i = i+1
	print(exact)
	table.to_csv("/home/meongeun/meshGeo/geofinal/final/npl.tsv", sep = '\t',)
#print(exact)
#print(mesh)
#print(s2d)
#print(mesh)
#print(xtree.find("Id").text)
#print(xtree.find("QueryKey").text)
#print(xtree.find("MeshHeading").text)
#print(xtree.find("Title"))	
#print(xtree.find("DocSum").find("Id").text)
#for i in xtree.find("Id"):
#	print(i.find("Id"))
#row.append({"count":count, "idList":idList})
#df = pd.DataFrame(rows,columns = ["count","idList"])



