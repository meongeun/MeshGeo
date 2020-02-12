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
df = pd.DataFrame({})

for k in r:
    nr.append(k.replace("/","")) 
    num.append(len(r))
for j in range(1,144):
	page = requests.get("https://ftp.ncbi.nih.gov/geo/series/GSE"+str(j)+'nnn'+"/")
	tree = html.fromstring(page.content)
	r = tree.xpath('//a/text()')
	#print(type(r))
	del r[0]
	num.append(len(r))
	for i in r:
		nr.append(i.replace("/","")) 
	#print(i)
#print(num)
#print(sum(num))

#print(nr)
#print(nr.index('GSE10974'))

series = pd.Series(nr)
series.to_csv('./nr.tsv',index=False,header=None,sep="\t")
