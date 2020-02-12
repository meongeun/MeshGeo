import pymysql
import requests
import pandas as pd

r = requests.get('http://stargeo.org/api/v2/series/?limit=10')
assert r.ok
data = r.json()

print(data['count'], len(data['results']))

print(data['results'][0])

r = requests.get(data['next'])

requests.get('http://stargeo.org/api/v2/series/GSE1/').text

samples_json = requests.get('http://stargeo.org/api/v2/series/GSE1/samples/').json()

# or 
samples = pd.read_json('http://stargeo.org/api/v2/series/GSE1/samples/')
print(samples.head())

host_name = localhost
#host_name = "SYSPHARM"
username = "root"
password = "1111"
database_name = "dave_db"
db = pymysql.connect(host=host_name, port=3306, user=username, passwd=password, db=database_name, charset='utf8')

print(db)


cursor = db.cursor()
print(cursor)

cursor.execute("set names utf8")
db.commit()

SQL_QUERY = """
DROP DATABASE IF EXISTS estate_db;
CREATE DATABASE estate_db DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

USE estate_db;
DROP TABLE IF EXISTS estate_db.estate;
CREATE TABLE estate_db.estate (
    estate_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    price INT NOT NULL,
    year CHAR(4) NOT NULL,
    dong VARCHAR(30) NOT NULL,
    apartname VARCHAR(30) NOT NULL,
    month CHAR(2) NOT NULL,
    day CHAR(5) NOT NULL,
    space VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    addresscode CHAR(5) NOT NULL,
    floor CHAR(3) NOT NULL,
    PRIMARY KEY(estate_id)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin
"""

cursor.execute(SQL_QUERY)
db.commit()

for item in items:
    estate_item = list()
    
    estate_item1 = item.find('거래금액').text.strip()
    estate_item2 = item.find('년').text.strip()
    estate_item3 = item.find('법정동').text.strip()
    estate_item4 = item.find('아파트').text.strip()
    estate_item5 = item.find('월').text.strip()
    estate_item6 = item.find('일').text.strip()
    estate_item7 = item.find('전용면적').text.strip()
    estate_item8 = item.find('지번').text.strip()
    estate_item9 = item.find('지역코드').text.strip()
    estate_item10 = item.find('층').text.strip()

    """
    sql = '''
        INSERT INTO estate_db.estate 
            (price, year, dong, apartname, month, day, space, address, addresscode, floor)
        VALUES 
            (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') 
    ''' % (int(estate_item1.replace(',', '')), estate_item2, estate_item3, estate_item4, estate_item5, estate_item6, estate_item7, estate_item8,
         estate_item9, estate_item10)
    # print(sql)
    cursor.execute(sql)
    db.commit()
    """





