import sys
import os

print ('The command line arguments are:')
for i in sys.argv:
	print i

print '\n\nThePYTHONPATH is', sys.path, '\n'

print 'The current directory is'
print os.getcwd()
