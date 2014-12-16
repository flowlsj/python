def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = raw_input("Please enter a string:")
if(is_palindrome(something)):
	print "Yes, it is palindrome"
else:
	print "Not a palindrome"
