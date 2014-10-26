data = open("singingghosts_tweets.txt").read()
data = data.replace("\n", " \n ")
words = [word for word in data.split(" ") if "http" not in word]
outfile = open("singingghosts_tweets_neat.txt", 'w')
for word in words:
	print(word, file=outfile, end=' ')
outfile.flush()
outfile.close()

