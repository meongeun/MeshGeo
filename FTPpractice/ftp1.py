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
#
ftp = ftplib.FTP('ftp.ncbi.nih.gov') 
ftp.login()

#sum = num[0]
for j in range(1,10):
        ftp.cwd('/geo/series/GSEnnn/'+'GSE'+str(j)) 
        filename = 'GSE'+str(j)+'_family.soft.gz'
        fd = open("./" + filename,'wb')
        #print(fd)
        ftp.retrbinary('RETR %s' % filename, fd.write)


#for i in range(1,144):
#	sum += num[i]
#	for j in nr[sum:sum+num[i]]:
#		ftp.cwd('/geo/series/GSE'+str(i)+'nnn/'+j) 
#		filename = j+'_family.soft.gz'
#		fd = open("./" + filename,'wb')
#		print(fd)
#		ftp.retrbinary("./geoData2"+filename, fd.write)
fd.close()

print("finish")
