from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys
import csv 
from collections import defaultdict

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
#i = 1

#ex = [['1','2'], ['2','3'], ['1','3'], ['3','4'], ['2','1'], ['3','1']]
#d = dict()
#for k, v in ex:
#	if k in d:
#		#ov = d[k]
#		#d[k] = [ov, v]
#		d[k].append(v)
#	else:
#		d[k] = [v]
#	writer = csv.writer(f, delimiter="\t")
#	writer.writerow((k,d[k]))
#	print(d)
d = dict()
#print(table_dic)
for gse, pmid in pubmedl[131:]:
	#print(gse, pmid)
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
	exact = list(mesh & s2d)	
	f = open("output_ff1.tsv", "a")
	writer = csv.writer(f, delimiter='\t')
	#print(list(exact))
	for e in exact:
		print(e + "   "+ gse)
		if e in d:
		#ov = d[k]
		#d[k] = [ov, v]
			d[e].append(gse)
		else:
			d[e] = [gse]
		writer.writerow((e,d[e],'D'))
	#print(d)

#	for l in list(exact):
#		print(l +"   "+ gse)
#		if l in table_dic:
#			table_dic[l].append(gse)
#		else:
#			table_dic[l] = [gse]
#		print(table_dic)
#		writer = csv.writer(f, delimiter="\t")
#		writer.writerow((l,table_dic[l]))
	#df = pd.DataFrame(table_dic)
	#df.to_csv('output.tsv', '\t', index=False)
#dff = pd.DataFrame(list(table_dic.items()), columns=['MeshID','GSE'])
#dff.to_csv('output_ff.tsv', '\t', index=False)	
	#print(table_dic)
		#table_dic[i].append(gse)

#	table.loc[i, 'GSE'] = gse
#	table.at[i, 'MeshID'] = list(exact)
#	table.loc[i, 'PubMed'] = pmid
#	table.loc[i, 'D/S'] = "D"
#	i = i+1
#	print(exact)
#	table.to_csv("/home/meongeun/meshGeo/geofinal/final/npl2.tsv", sep = '\t',)
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



