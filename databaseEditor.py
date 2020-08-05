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
		 
		print("You added: ",end="")
		database.findByName(sirname)
		
	if (inpt == "updatePay"):
		name = input("Name: ")
		sirname = input("Sirname: ")
		pay = int(input("New Sallary: "))
		
		database.updatePay(name,sirname,pay)

		print("Updated: ",end="")
		database.findByName(sirname)

		database.findByName(sirname)

	if(inpt =="deleteEmployee"):
		sirname =input("Sirname: ")

		print("Deleted: ",end="")
		database.findByName(sirname)

		database.delete(sirname)

	if(inpt =="deleteAll"):

		print("Deleted: ")

		database.showAll()

		database.deleteAll()

