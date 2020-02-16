import pandas as pd

df1 = pd.read_csv('../NLP/nlp_me_71_5.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df1.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df2 = pd.read_csv('../NLP/nlp_me_71_6.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df2.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df3 = pd.read_csv('../../Downloads/nlp_me_71_2p.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df3.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df4 = pd.read_csv('../../Downloads/nlp_me_71_1b.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df4.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df5 = pd.read_csv('../../Downloads/nlp_me_71_b.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df5.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df6 = pd.read_csv('../../Downloads/nlp_me_71_4k.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df6.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df7 = pd.read_csv('../../Downloads/nlp_me_71_3k.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df7.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df8 = pd.read_csv('../../Downloads/nlp_me_71_2a.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df8.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df9 = pd.read_csv('../../Downloads/nlp_me_71_3a.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df9.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df10 = pd.read_csv('../../Downloads/nlp_me_71_4a.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df10.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
df11 = pd.read_csv('../../Downloads/nlp_me_71_p.tsv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
df11.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
#mesh1 = pd.concat([df1,df2, df3, df4, df5, df6])
#mesh1.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
#dumesh1 = mesh1.drop_duplicates(['ID', 'GSE', 'Synonym','Score'], keep='last')
#dumesh1.to_csv("../NLP/nlp_me_du1.tsv", sep='\t', index=False)
#
#mesh2 = pd.concat([df7, df8, df9, df10, df11])
#mesh2.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
#dumesh2 = mesh2.drop_duplicates(['ID', 'GSE', 'Synonym','Score'], keep='last')
#dumesh2.to_csv("../NLP/nlp_me_du2.tsv", sep='\t', index=False)
#
mesh = pd.concat([df1,df2, df3, df4, df5, df6, df7, df8, df9, df10, df11])
mesh.columns = ['ID', 'GSE', 'Synonym','Score', 'D/S']
dumesh = mesh.drop_duplicates(['ID', 'GSE', 'Synonym','Score'], keep='last')
dumesh.to_csv("../NLP/nlp_me_du.tsv", sep='\t', index=False)

