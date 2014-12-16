poem = '''\
	   Programming is fun
	   If you enjoy it
	   But for NN,
	   It is nightmare
'''

# open for 'w'riting
f = open('../poem.txt', 'w')
f.write(poem)
f.close()

f = open('../poem.txt', 'r')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
f.close()
