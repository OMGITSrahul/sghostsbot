## init
from twitter import *
import os
import time
print("clock started")
starttime = time.time()
outfile = open("singingghosts_tweets.txt", 'w')

## application keys

keys = [['BOf9HtUQitquRvU3VabWSi4xt', 'uwwlIUbasYdxL5HIDQkgpFa11g1ODzIBfsBb7rXJgDcyt2wYCW'],
		['bXjQy7vnawlR7gFquS6lHG9Ts', 'dDVav0sTQypTBMkqZzaGhbW4HYnb1hSyNdFszdENR60g0RsP5u'],
		['adlnAJVa4OjvG4oXeEAvCFFZC', 'v4rmVckBCHt6W3a226LsKpiYvHAN0am8TbzoebCd3zGHYYN4gm']]
## auth sequence
def secrets(i):
	CONSUMER_KEY = keys[i][0]
	CONSUMER_SECRET = keys[i][1]

	MY_TWITTER_CREDS = os.path.expanduser('~/.twittercreds_'+str(i-1))

	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

	return oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET

def client(i):
	oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET = secrets(i)
	twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

	return twitter

first = 0

for i in range(0, 3):
	twitter = client(i)
	print("client ",i," created and ready in ", round(time.time()-starttime, 3), "s", sep='')
	if first == 0:
		tweets_raw = twitter.statuses.user_timeline(screen_name="singing_ghosts", include_rts=False, exclude_replies=True)
		tweets = [[tweet['text'], tweet['id_str']] for tweet in tweets_raw]
		last = tweets[-1][1]
		for tweet in tweets:
			tweettext = tweet[0].replace("&amp;", "&")
			print(tweettext, file=outfile)
		total = len(tweets)
		print("retrieved ",total," tweets in ", round(time.time()-starttime, 3), "s", sep='')
		first = 1
	try:
		while tweets != []:
			tweets_raw = twitter.statuses.user_timeline(screen_name="singing_ghosts", include_rts=False, exclude_replies=True, max_id=last)
			tweets = [[tweet['text'], tweet['id_str']] for tweet in tweets_raw]
			last = tweets[-1][1]
			for tweet in tweets:
				tweettext = tweet[0].replace("&amp;", "&")
				print(tweettext, file=outfile)
			total += len(tweets)
			print("retrieved ",total," tweets in ", round(time.time()-starttime, 3), "s", sep='')
	except:
		pass
	print("client", i, "hit rate limit, switching clients now")
outfile.close()
print("retieved", total, "tweets in", round(time.time()-starttime, 3), "seconds,", "\nEND")
