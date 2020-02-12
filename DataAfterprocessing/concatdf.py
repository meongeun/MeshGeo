import pandas as pd 
df1 = pd.read_csv("../Downloads/output_ff1.tsv", '\t')
df2 = pd.read_csv("../Downloads/output_ff2.tsv", '\t')
final = pd.concat([df1, df2])
final.to_csv('../Downloads/output_con.tsv', sep='\t', index=False, header =False)
