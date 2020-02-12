import gzip
import zipfile
f = gzip.open('./geoData2/GSE73976_family.soft.gz','rt')
for i in range(0,50):
	line = f.readline()
	print(line)
