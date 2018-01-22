class Employee():
	
	def __init__(self,first,last,salary):
		
		self.first = first
		self.last = last
		self.salary = salary
		
	def give_raise(self):
		self.salary += 5000
		print(str(self.salary))
		
	def full_name(self):
		f_name = self.first + self.last
		print(f_name.title())
		
man = Employee('abhi','walia',5000)
man.full_name()
man.give_raise()
