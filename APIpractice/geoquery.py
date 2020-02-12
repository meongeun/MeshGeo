from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.request import urlopen
import requests
import pandas as pd
import urllib.request
from lxml import html

db ='pubmed'
qstr = 'asthma[mesh]+AND+leukotrienes[mesh]+AND+2009[pdat]'
term = 'cancer[All+fields]' 
base = 'https://www.ncbi.nlm.nih.gov/gds?'
#thing = urlretrieve(base+"&term={term}")

page = requests.get(base+"&term={term}")
#print(r)
#print(thing)
tree = html.fromstring(page.content)
rescs = tree.xpath('//div[@class="resc"]/dl[@class="rprtid"]/dd/text()')
#response = urlopen(base+"&term={term}").read()
#xtree = ET.fromstring(response)
#print(xtree)
print(rescs)

fp = urllib.request.urlopen(base+"&term={term}")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

#print(mystr)



