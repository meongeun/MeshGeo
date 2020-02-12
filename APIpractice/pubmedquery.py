from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import sys

db ='pubmed'
pmid = '28755519' 
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

response = urlopen(base+"esummary.fcgi?db="+db+"&id="+pmid).read()
xtree = ET.fromstring(response)
print(xtree)

#print(xtree.find("Id").text)
#print(xtree.find("QueryKey").text)
#print(xtree.find("MeshHeading").text)
#print(xtree.find("Title"))	
#print(xtree.find("DocSum").find("Id").text)
#for i in xtree.find("Id"):
#	print(i.find("Id"))
#row.append({"count":count, "idList":idList})
#df = pd.DataFrame(rows,columns = ["count","idList"])



