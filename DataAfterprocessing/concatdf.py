import pandas as pd 
df1 = pd.read_csv("../final/your_no.tsv", '\t')
df2 = pd.read_csv("../../Downloads/me.csv", '\t')
final = pd.concat([df1, df2])
final.to_csv('../../Downloads/final_con_final.tsv', sep='\t', index=False)
