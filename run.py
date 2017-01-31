import csv

with open('input.txt','rb') as f:
	input = f.readlines()
input = [x.strip() for x in input]

ranks={}
with open('additional/finalrelchi230.csv', 'rb') as tweetfile:
		reader1 = csv.reader(tweetfile)
		for row in reader1:
				ranks[row[0]]=row[6]

myfile = open('output.csv', 'wb')
myfile.close()

output={}
for word in input:
	output[word]=ranks[word]

count=1

myfile = open('output.csv', 'a')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(["Word","Rank"])
myfile.close()

for key1 in sorted(output, key=output.get,reverse=True):
	myfile = open('output.csv', 'a')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	csvrow=[]
	csvrow.append(key1)
	csvrow.append(count)
	wr.writerow(csvrow)
	myfile.close()
	count+=1
