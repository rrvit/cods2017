'''
This file is used to generate two files which contain unique english and hindi words
'''
#Some tweets have special characters which python is not able to read. Therefore, that might lead to a minute percent of error
import csv
import pprint

count=0;
tweets={}       #Tweets is a dictionary with index as tweetid and corresponding tweet as value
validenglishwordlist=[]
validhindiwordlist=[]
uniquehindivalidwordlist=[]
uniqueenglishvalidwordlist=[]

#import Tweets in a list
with open('tweets_all.csv', 'rb') as tweetfile:                 
    reader1 = csv.reader(tweetfile)
    for row in reader1:
        tweets[row[0]]=row[1]

#Form words from stream positions given in datasheet
with open('Datasheet.csv', 'rb') as posfile:
    reader2=csv.reader(posfile)
    for row in reader2:
        print count
        if count>len(tweets):               #Only run datasheet till the number of imported tweets
            break
        else:
            currenttweetid=row[0]
            for y in range(1,(len(row))):
                if currenttweetid in tweets:
                    startpos=''
                    endpos=''
                    lang=''
                    firstcol=0
                    secondcol=0
                    for char in row[y]:
                        if char!=':' and firstcol==0:
                            startpos+=char
                        elif char!=':' and firstcol==1 and secondcol==0:
                            endpos+=char
                        elif char!=':' and firstcol==1 and secondcol==1:
                            lang+=char
                        elif char==':' and firstcol==0:
                            firstcol=1
                        elif char==':' and firstcol==1:
                            secondcol=1
                    word=''
                    #x=repr(tweets[currenttweetid])
                    #print x
                    #print startpos
                    #print endpos
                    #x1= x.replace('\\xc2\\xa0','')
                    #x2= x1.replace('\\xc2',' ')
                    #y= x2.replace('\\xa0',' ')
                    #z=eval(y)
                    #print z
                    if lang!='OTHER' and tweets[currenttweetid]!='Error' and tweets[currenttweetid]!='' and (lang=='EN' or lang=='HI'):
                        for x in range(int(startpos)-1,int(endpos)):
                            try:
                                word+=tweets[currenttweetid][x]
                            except:
                                print currenttweetid
                        #For testing purposes: Here due to the specal character, error is created.
                        #If code doesn't work, comment this test area completely
                        #print word
                        '''
                        if currenttweetid=='565428778235887617':        
                            print startpos+endpos+lang
                            #print word
                            #test=unicode(tweets[currenttweetid], "utf-8")
                            #try:
                            print tweets[currenttweetid]
                            x=repr(tweets[currenttweetid])
                            #y= x.replace('\\xc2\\xa0', ' ')
                            #print y
                            y=eval(x)
                            print y[60]
                            #print tweets[currenttweetid][62]
                            #except:
                                #print "hello"
                        #Test code ends'''
                    if lang=='EN':
                        validenglishwordlist.append(word)
                    elif lang=='HI':
                        validhindiwordlist.append(word)                
        count+=1

#Create unique word files
for word in validenglishwordlist:
      if not word in uniqueenglishvalidwordlist:
          uniqueenglishvalidwordlist.append(word);
myfile = open('uniqueenglishvalidwordlist.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(uniqueenglishvalidwordlist)

for word in validhindiwordlist:
      if not word in uniquehindivalidwordlist:
          uniquehindivalidwordlist.append(word);
myfile = open('uniquehindivalidwordlist.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(uniquehindivalidwordlist)

