import os
import pandas as pd

nd = pd.read_csv('nd.tsv',sep='\t').values.tolist()
	
for i in nd[32001:49999]:
	file = './geoData2/'+str(i[0])+'_family.soft.gz'
	if os.path.isfile(file):
		os.remove(file)	

for i in nd[93000:]:
    file = './geoData2/'+str(i[0])+'_family.soft.gz'
    if os.path.isfile(file):
        os.remove(file) 

