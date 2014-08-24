from twitter import *
import os
import time
## application keys

keys = [['BOf9HtUQitquRvU3VabWSi4xt', 'uwwlIUbasYdxL5HIDQkgpFa11g1ODzIBfsBb7rXJgDcyt2wYCW']]
## auth sequence
def secrets(i):
	CONSUMER_KEY = keys[i][0]
	CONSUMER_SECRET = keys[i][1]

	MY_TWITTER_CREDS = os.path.expanduser('~/.botcreds_'+str(i))

	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("beanad_ebooks", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

	return oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET

def client(i):
	oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET = secrets(i)
	twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

	return twitter

def opener():
	infile = open("./tweets/beanad_ebooks_approved_1.txt")
	data = infile.read()
	infile.close()
	tweets = data.split("|")
	return tweets

def sendtweet(tweet, twitter):
		try:
			twitter.statuses.update(status=tweet, lat=31.7031, long=35.1956)
			return True
		except:
			return False

def exit(tweets):
	outfile = open("./tweets/beanad_ebooks_approved_1.txt", 'w')
	for tweet in tweets:
		print(tweet, file=outfile, end="|")
	outfile.close()

sent = 0

try:
	number = int(input("how many tweets do you want to send? "))
	delay = int(input("how many minutes between tweets?"))*60
	tweets = opener()
	twitter = client(0)
	while sent < number:
		tweet = tweets[0]
		print('\n"', tweet, '"', sep="")
		result = sendtweet(tweet, twitter)
		if result:
			sent += 1
			dead = tweets.pop(0)
			print(sent, "tweets sent.")
			if sent < number:
				time.sleep(delay)
		else:
			print("Hold on")
			time.sleep(60)
	exit(tweets)
	print("quit")

except:
	exit(tweets)
	print("quit")
