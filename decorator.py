def decorator(method):
	print "Hello, I am decorator printing"
	return method

@decorator
def func():
	print "I am func() printing"

func()
