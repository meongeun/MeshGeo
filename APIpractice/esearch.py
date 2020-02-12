import entrezpy.esearch.esearcher

tool = "pipeline"
email ='meongeun7@gmail.com'
apiKey = 'b323216e4dcf62321679cdf20ebda3182b08'
apiKey_var = 'b323216e4dcf62321679cdf20ebda3182b08'
threads = 5
e = entrezpy.esearch.esearcher.Esearcher(tool,
                                         email,
                                         apikey=None,
                                         apikey_var=None,
                                         threads=None,
                                         qid=None)

analyzer = e.inquire({'db' : 'pubmed',
                      'id' : [17284678, 9997],
                      'retmode' : 'text',
                      'rettype' : 'abstract',
					  'usehistory':'y'
						})
print(analyzer.count, analyzer.retmax, analyzer.retstart, analyzer.uids)

