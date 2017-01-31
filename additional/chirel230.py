import csv
import re                                                       #for string processing

ncme=167148
ncmh=19603
ncmecmh=ncme+ncmh
cme=[]
cmh=[]
cmh3=[]
cme3=[]
englishwords=[]
count=0

with open('230words.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

with open('CME.csv', 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
                cme+=row
                count+=1
                print count

count=0

with open('CMH.csv', 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
                cmh+=row
                count+=1
                print count

count=0

with open('uniqueenglishvalidwordlist.csv', 'rb') as tweetfile:
        reader1 = csv.reader(tweetfile)
        for row in reader1:
            englishwords+=row
            count+=1
            print count

myfile = open('finalrelchi230.csv', 'wb')        #To empty the file first
myfile.close()

for cmh1 in cmh:
        cmh2=re.findall(r"[\w']+", cmh1)
        cmh3+=cmh2

for cme1 in cme:
        cme2=re.findall(r"[\w']+", cme1)
        cme3+=cme2


print "Starting Relevance Calculation"

for word in content:
	print word 
        if word in cme3:
                a=0
                for word1 in cme3:
                        if word==word1:                                                 
                                a+=1
		print "a"+str(a)
		b=ncme-a					
		print "b"+str(b)
                c=0
                for word1 in cmh3:
                        if word==word1:
                                c+=1
		print "c"+str(c)
		d=ncmh-c					
                e1=(a+b)*(a+c)/float(ncmecmh)			
		e2=(a+b)*(b+d)/float(ncmecmh)
                e3=(c+d)*(a+c)/float(ncmecmh)
                e4=(c+d)*(b+d)/float(ncmecmh)

                chi=((a-e1)*(a-e1)/e1)+((b-e2)*(b-e2)/e2)*((c-e3)*(c-e3)/e3)+((d-e4)*(d-e4)/e4)
                relevance11=(a/e1)
		relevance21=(c/e3) 
		print chi
                myfile = open('finalrelchi230.csv', 'a')
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                csvrow=[]
                csvrow.append(word)
                csvrow.append(a)
                csvrow.append(b)
                csvrow.append(c)
		csvrow.append(d)
                csvrow.append(relevance11)
		csvrow.append(relevance21)
		csvrow.append(chi)
                wr.writerow(csvrow)
                myfile.close()
