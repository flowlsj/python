class CustomException(Exception):
	'''A user-defined exception'''
	def __init__(self, error):
		self.error = error

try:
	userMsg = raw_input("Please enter the command:\n")
	if(userMsg == "Custom"):
		raise CustomException("User defined exception")
	else:
		raise Exception()
except CustomException:
	print "Caught an exception"
except:
	print "Other exception caught"
else:
	print "No exception caught"
