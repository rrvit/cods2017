import csv
import re 							#for string processing
#Create vector for English words
tweets={}
with open('tweets_all.csv', 'rb') as tweetfile:
	reader1 = csv.reader(tweetfile)
	for row in reader1:
		tweets[row[0]]=row[1]

englishwords=[]
with open('uniqueenglishvalidwordlist.csv', 'rb') as tweetfile:
	reader1 = csv.reader(tweetfile)
	for row in reader1:
	    englishwords+=row

hindiwords=[]
with open('uniquehindivalidwordlist.csv', 'rb') as tweetfile:
	reader1 = csv.reader(tweetfile)
	for row in reader1:
	    hindiwords+=row

myfile = open('tweetlang.csv', 'wb')	#To empty the file first
myfile.close()

#Find Chi square variables
for tweetid, tweet in tweets.iteritems():
	tweet1=re.findall(r"[\w']+", tweet)
	hindiwordcount=0
	englishwordcount=0
	tweet2=list(enumerate(tweet1))				#Temporary list of tweet words to check code switching
	tweet2.pop()								#Popping last element helps in iterating easily
	print tweet1+tweet2
	codeswitch=0
	for index, word in tweet2:
		if (word in hindiwords and tweet1[index+1] in englishwords) or (word in englishwords and tweet1[index+1] in hindiwords):
			codeswitch=+1
	if codeswitch>1:
		lang="CDS"
	else:
		for word in tweet1:
			if word in hindiwords:
				hindiwordcount+=1
			if word in englishwords:
				englishwordcount+=1
		if englishwordcount+hindiwordcount!=0:
			engwordpercent=englishwordcount/float(englishwordcount+hindiwordcount)
			hindiwordpercent=hindiwordcount/float(englishwordcount+hindiwordcount)
		else:
			engwordpercent=0
			hindiwordpercent=0
		lang="untagged"
		if(engwordpercent>0.9):
			lang="EN"
		elif(hindiwordpercent>0.9):
			lang="HI"
		elif(engwordpercent>0.5):
			lang="CME"
		elif(hindiwordpercent>0.5):
			lang="CMH"
		elif(hindiwordpercent==engwordpercent):
			lang="CMEQ"
	myfile = open('tweetlang.csv', 'a')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	csvrow=[]
	csvrow.append(tweetid)
	csvrow.append(tweet)
	csvrow.append(lang)
	wr.writerow(csvrow)
	myfile.close()

