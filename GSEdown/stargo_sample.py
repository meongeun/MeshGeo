import requests
import pandas as pd

r = requests.get('http://stargeo.org/api/v2/series/?limit=10')
assert r.ok
data = r.json()

print(data['count'], len(data['results']))

for i in data['results']:
	print(data['series'])

r = requests.get(data['next'])

requests.get('http://stargeo.org/api/v2/series/GSE1/').text

samples_json = requests.get('http://stargeo.org/api/v2/series/GSE1/samples/').json()
# or 
samples = pd.read_json('http://stargeo.org/api/v2/series/GSE1/samples/')
print(samples.head())
print(type(samples.head()))




