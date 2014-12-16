try:
	text = raw_input("Enter something...")
except EOFError:
	print "EOF got!"
except KeyboardInterrupt:
	print "You cancelled the thread"
else:
	print "You entered: {}".format(text)
