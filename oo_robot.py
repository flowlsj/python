class Robot:
	population = 0
	def __init__(self, name):
		self.name = name
		Robot.population += 1
		print "Robot {0} has been created".format(self.name)
	def destroy(self):
		Robot.population -= 1
		print "I am {}, I am being destroied".format(self.name)
	@classmethod
	def count(cls):
		print "cls is", cls
		print "There are {:d} robots still alive".format(cls.population)

bee = Robot("Bee")
bee.count()

ironMan = Robot("IronMan")
ironMan.count()

bee.destroy()
Robot.count()

ironMan.destroy()
Robot.count()
