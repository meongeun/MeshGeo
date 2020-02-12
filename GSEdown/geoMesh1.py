import GEOparse
import pymysql
import requests
from bs4 import BeautifulSoup

#host_name = "SYSPHARM"
#username = "root"
#password = "1111"
#database_name = "geomesh1_db"
#db = pymysql.connect(host=host_name, port=3306, user=username, passwd=password, db=database_name, charset='utf8')
#print(db);

#cursor = db.cursor()
#cursor.execute("set names utf8")
#db.commit()
#PATH_TO_FILE = 'meshsqlscript'
#for line in open(PATH_TO_FILE):
#    cursor.execute(line)
#db.commit()


for i in range(1,2):
	gse = GEOparse.get_GEO(geo="GSE"+str(i), destdir="./geoData")
#return filepath, getype
#url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+str(i)
#resp = requests.get(url)
#html = resp.text

#soup = BeautifulSoup(html, "lxml")
#tables = soup.find("table").td.children
#trs = tables.find_all('tr')
#print(tables) 
#tag = soup.find('td')
#print(tag.get_text().strip())

#soup.find('p')
#print(soup.find('td', style = "text-align: justify"))    #속성을 줌
#soup.find('div', class_='test')
#attrs = {'id': 'viewer', 'class':'test'}
#soup.find('div', attrs = attrs) #multi 속성
#soup.find_all('p')  #리스트 형식으로 반환
#soup.find_all('div', class_='test')

#attribute값 추출
#tag = soup.find('h3')
#print(tag)
#tag['title']

#print(gse.title)
#print("GSM example:")
#print(gse.gsms.items())

##for gsm_name,gsm in gse.gsms.items():
#    print("Name: ", gsm_name)
#    print("Metadata:",)
#    for key, value in gsm.metadata.items():
#        print(" - %s : %s" % (key, ", ".join(value)))
#    print ("Table data:",)
#    print (gsm.table.head())
#    print()
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

