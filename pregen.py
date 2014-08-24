outfile = open("./tweets/beanad_ebooks_batch_2.txt", 'w')
data = open("beanad_tweets_neat.txt").read()
import dpress
import os
import time
def gen():
	try:
		twee = dpress.main(data)
	except:
		twee = dpress.main(data)

	temp = open("temp", 'w')
	print(twee, file=temp)
	temp.close()

	tweet = os.popen("./dadadodo/dadadodo -c 1 ./temp").read().strip()

	if len(tweet) <141:
		#print("#",twee, "#")
		return tweet
	else:
		return gen()
		
	
tweets = []
while len(tweets) < 5:
	tweet = gen()
	if tweet != None and "downfall sext" not in tweet and tweet not in tweets:
		tweets.append(tweet)

	time.sleep(0.02)
for tweet in tweets:
	print(tweet, len(tweet))
	print(tweet, end="|", file=outfile)
outfile.close()