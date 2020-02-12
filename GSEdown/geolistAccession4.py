import GEOparse

import ftplib
import os

from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import pandas as pd
import urllib.request
from lxml import html

page = requests.get("https://ftp.ncbi.nih.gov/geo/series/GSE"+'nnn'+"/")
tree = html.fromstring(page.content)
r = tree.xpath('//a/text()')
del r[0]
num = []
nr = []

#for k in r:
#    nr.append(k.replace("/","")) 
#    num.append(len(r))
#
#for j in range(1,144):
#    page = requests.get("https://ftp.ncbi.nih.gov/geo/series/GSE"+str(j)+'nnn'+"/")
#    tree = html.fromstring(page.content)
#    r = tree.xpath('//a/text()')
#    #print(type(r))
#    del r[0]
#    num.append(len(r))
#    for i in r:
#        nr.append(i.replace("/",""))
#print("array 생성완료 ")

#nr = pd.read_csv('./nr.tsv', sep='\t').values.tolist()
nd = pd.read_csv('nd.tsv',sep='\t').values.tolist()
for i in nd[75000:82000]:
	gse = GEOparse.get_GEO(geo=i[0], destdir="/drive/My Drive/geoData5")
	print(str(i))

#return filepath, getype

#print()
#print("GSM example:")
#for gsm_name,gsm in gse.gsms.items():
#    print("Name: ", gsm_name)
#    print("Metadata:",)
#    for key, value in gsm.metadata.items():
#        print(" - %s : %s" % (key, ", ".join(value)))
#    print ("Table data:",)
#    print (gsm.table.head())
#    break

#print()
#print("GPL example:")
#for gpl_name, gpl in gse.gpls.items():
#    print("Name: ", gpl_name)
#    print("Metadata:",)
#    for key, value in gpl.metadata.items():
#        print(" - %s : %s" % (key, ", ".join(value)))
#    print("Table data:",)
#    print(gpl.table.head())
#    break





