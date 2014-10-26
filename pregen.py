outfile = open("./tweets/sghosts_ebooks_batch_1.txt", 'w')
data = open("./tweets/singingghosts_tweets_neat.txt").read()
import dpress
import os
import time
def gen():
	twee = 0
	while twee == 0:
		try:
			twee = dpress.main(data)
		except:
			time.sleep(0.8)
	temp = polltemp()
	if temp > 93.0:
		cooldown()

	temp = open("temp", 'w')
	print(twee, file=temp)
	temp.close()

	tweet = os.popen("./dadadodo/dadadodo -c 1 ./temp").read().strip()

	if len(tweet) <141:
		#print("#",twee, "#")
		return tweet
	else:
		return gen()
		
	
def polltemp():
	temps = os.popen("sensors").read().split("\n")[11:13]

	temps_raw = []

	for line in temps:
		line = line.split("+")
		temporary = []
		for snippet in line:
			snippet = snippet.split("°")
			temporary.append(snippet)
		try:
			temps_raw.append(float(temporary[1][0]))
		except:
			temps_raw.append(100.0)
	high = max(temps_raw)
	return high

def cooldown():
	time.sleep(1)
	temp = polltemp()
	while temp >80.0:
		time.sleep(5)
		temp = polltemp()


tweets = []
while len(tweets) < 500:
	temp = polltemp()
	if temp > 93.0:
		cooldown()
	tweet = gen()
	if tweet != None and "downfall sext" not in tweet and tweet not in tweets:
		tweets.append(tweet)
	if not(len(tweets) % 5):
		print(len(tweets))

for tweet in tweets:
	print(tweet, len(tweet), "#", len(tweets))
	print(tweet, end="|", file=outfile)
outfile.close()