class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def printSelf(self):
		print 'My name is:', self.name,\
			'I am ', self.age

p = Person('Louis', 28)
p.printSelf()
