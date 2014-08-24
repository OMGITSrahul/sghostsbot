def opener():
	infile = open("./tweets/beanad_ebooks_batch_1.txt")
	data = infile.read()
	infile.close()
	tweets = data.split("|")
	return tweets

def sendtweet(tweet, outfile):
		print(tweet, file=outfile, end="|")
		outfile.flush()

def exit(tweets):
	outfile = open("./tweets/beanad_ebooks_batch_1.txt", 'w')
	for tweet in tweets:
		print(tweet, file=outfile, end="|")
	outfile.close()

sent = 0
tweets = opener()
try:
	approved = open("./tweets/beanad_ebooks_approved_1.txt", 'w')
	while sent < 100:
		tweet = tweets.pop(0)
		print('\n"', tweet, '"', sep="")
		dec = input("tweet?[y/n]: ")

		if dec == 'y' or dec == '':
			sendtweet(tweet, approved)
			sent += 1
			print(sent, "tweets sent.")

	exit(tweets)
	approved.close()
	print("quit")

except:
	exit(tweets)
	approved.close()
	print("quit")
