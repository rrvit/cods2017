import csv

myfilecme = open('CME.csv', 'wb')
wrcme = csv.writer(myfilecme, quoting=csv.QUOTE_ALL)

myfilecmh = open('CMH.csv', 'wb')
wrcmh = csv.writer(myfilecmh, quoting=csv.QUOTE_ALL)

myfileen = open('EN.csv', 'wb')
wren = csv.writer(myfileen, quoting=csv.QUOTE_ALL)

myfilehi = open('HI.csv', 'wb')
wrhi = csv.writer(myfilehi, quoting=csv.QUOTE_ALL)

myfilecmeq = open('CMEQ.csv', 'wb')
wrcmeq = csv.writer(myfilecmeq, quoting=csv.QUOTE_ALL)

with open('tweetlang.csv', 'rb') as tweetfile:                 
    reader1 = csv.reader(tweetfile)
    for row in reader1:
        if row[2]=="CME":
            wrcme.writerow(row)
        elif row[2]=="CMH":
            wrcmh.writerow(row)
	elif row[2]=="EN":
            wren.writerow(row)
	elif row[2]=="HI":
            wrhi.writerow(row)
	elif row[2]=="CMEQ":
            wrcmeq.writerow(row)

myfilecme.close()
myfilecmh.close()
myfileen.close()
myfilehi.close()
myfilecmeq.close()
