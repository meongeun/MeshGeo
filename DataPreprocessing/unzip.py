import gzip
gb_file = gzip.open('./geoData/GSE410_family.soft.gz','rb')
for i in gb_file.readlines():
	print(i)
print(gb_file)


