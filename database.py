import sqlite3
from employeeCreate import Employee


class Database:
	#####################
	def __init__(self):
		self.conn = sqlite3.connect('employees.db')
		self.c = self.conn.cursor()
		self.employees = []
		try:
			self.c.execute("""CREATE TABLE employees(
			             first text,
			             last text,
			             pay integer
						)""")
		except:
			pass
		
		

	def addEmployee(self,name,sirname,pay):
		emp =Employee(name, sirname, pay)
		self.employees.append(emp)
		self.c.execute("INSERT INTO employees VALUES (? ,? ,? )",(name, sirname, pay))
		self.conn.commit()


	def showAll(self):
		self.c.execute("SELECT * FROM employees")
		for a,b,c in self.c.fetchall():
			print(a,b,c)
			
	def delete(self,sirname):
		self.c.execute("DELETE FROM employees WHERE last =?",(sirname,))
		self.conn.commit()

	def deleteAll(self):
		self.c.execute("DELETE FROM employees")
		self.conn.commit()

	def findByName(self,sirname):
		self.c.execute("SELECT * FROM employees WHERE last =?",(sirname,))
		for a,b,c in self.c.fetchall():
			print(a,b,c)

	def updatePay(self,name,sirname,pay):
		self.c.execute("UPDATE employees SET pay =? WHERE first =? AND last =?",(pay,name,sirname))
		self.conn.commit()

	
