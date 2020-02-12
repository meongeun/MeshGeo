import pandas as pd

mesh = pd.read_csv('../Downloads/output_con.tsv', sep='\t')
mesh.columns = ['MeshID', 'GSE', 'D/S']
dumesh = mesh.drop_duplicates(['MeshID'], keep='last')
dumesh.to_csv("../Downloads/output_du.tsv", sep='\t', index=False)

