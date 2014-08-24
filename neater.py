import re
infile = open("beanad_ebooks_0.8.txt")
outfile = open("beanad_ebooks_0.8_.txt", 'w')

dirty = infile.read()

clean = "\n\n".join([line for line in dirty.split("|")])


print(clean, file=outfile)
print(len(clean.split(" ")))
outfile.close()
