class Employee:

	def __init__ (self,first,last,pay):
		self.first= first
		self.last = last
		self.pay = pay
	

	def createEmail(self):
		return f'{self.first}.{self.last}@gmail.com'


