import GEOparse

#i=1
for i in range(204,14000):
	gse = GEOparse.get_GEO(geo="GSE"+str(i), destdir="./geoData")
#return filepath, getype

#print()
#print("GSM example:")
#for gsm_name,gsm in gse.gsms.items():
#    print("Name: ", gsm_name)
#    print("Metadata:",)
#    for key, value in gsm.metadata.items():
#        print(" - %s : %s" % (key, ", ".join(value)))
#    print ("Table data:",)
#    print (gsm.table.head())
#    break

#print()
#print("GPL example:")
#for gpl_name, gpl in gse.gpls.items():
#    print("Name: ", gpl_name)
#    print("Metadata:",)
#    for key, value in gpl.metadata.items():
#        print(" - %s : %s" % (key, ", ".join(value)))
#    print("Table data:",)
#    print(gpl.table.head())
#    break





