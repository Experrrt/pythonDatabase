import database

database = database.Database()

while True:
	inpt =input(">")
	
	if inpt =="showAll":
		database.showAll()
	
	if(inpt=="addEmployee"):
		 name = input("Name: ")
		 sirname = input("Sirname: ")
		 pay = int(input("Sallary: "))
		 
		 database.addEmployee(name,sirname,pay)
		 
		 print("You added: ",end='')
		 
		 database.findByName(sirname)