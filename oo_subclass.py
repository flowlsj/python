class Engineer:
	'''This is the base class of all engineer'''
	def __init__(self, name, title):
		'''Initiate an engineer'''
		self.name = name
		self.title = title
		print "Initiate an engineer named: {}".format(self.name)
	def tell(self):
		'''Tell myself'''
		print "I am an enineer, my name is: {0}, my title is: {1}".\
			format(self.name, self.title)
			
class SoftwareEngineer(Engineer):
	'''This is the class of software enginerr'''
	def __init__(self, name, title, tool):
		'''Initiate a software engineer'''
		Engineer.__init__(self, name, title)
		self.tool = tool 
	def tell(self):
		'''Tell myself'''
		Engineer.tell(self)
		print "My tool is:", self.tool

class HardwareEngineer(Engineer):
	'''This is the class of hardware enginerr'''
	def __init__(self, name, title, platform):
		'''Initiate a hardware engineer'''
		Engineer.__init__(self, name, title)
		self.platform = platform
	def __tell__(self):
		'''Tell my self'''
		Engineer.tell(self)
		print "I work on:", self.platform	

se = SoftwareEngineer('Louis','Senior software engineer','Computor' )
se.tell()
he = HardwareEngineer('John','Electronic engineer', 'Intel chipsets')
he.tell()
