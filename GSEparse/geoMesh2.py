
f = open("./geoData/GSE1/soft/GSE1_family.soft", 'r')

while True:
    line = f.read()
    if not line: break
    print(line)

f.close()

