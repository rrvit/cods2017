Instructions to run the file:

Softwares Required:
Python 2.7

The 'input.txt' should include candidate words separated by newline (“\n”).
Execute the 'run.py' in the python compiler.
After executing the code it will generate a comma separated text file output.csv. Each row of output.csv contains candidate word and the calculated rank for that word separated by a commas.
Please note that the input file must contain words from the given 230 words.

For comipiling the complete code again, follow steps below:

1. Run the 'importtweets.py'. Additional Tweepy library is needed to run this code. Also, access tokens for twitter might have expired, so please generate and update the same in the code. This code will download all tweets one by one from twitter and might run for even a day or two. tweets_all.csv will be generated.

2. Run the 'generatewordlist.py' file. This will generate two new files-'uniqueenglishvalidwordlist.csv' and 'uniquehindivalidwordlist.csv'.

3. Next, run 'tweetlangtag.py'. This will create a new file named tweetlang.csv.

4. Run the 'seperatecmeandcmh.py' file which will generate seperate files for all the categories of tweets.

5. Run the 'chirel230.py' file. '230words.txt' file is used as input here. '230words.txt' should contain all the words for which ranking is required. The ranking will be generated in the 'finalrelchi230.csv' file. The borrowing index is the seventh column of each row. 

6. Finally, run the 'run.py' file in the root folder. Make sure that 'input.txt' should contain all the words for which ranking is required and is a subset of '230words.txt'.