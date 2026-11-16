#this is the exercies 1 for lecture 16
#with the aid of a function and a dictionary, write an interactive python 
#programme/script that will ask the user the following questions
def interrogate():
	#1.what's your name?
	name=input("1.what's your name?\n")
	age=input("2.how old are you?\n")
	color=input("3.what is your favourite colour?\n")
	python=input("4.do you like python?\n")
	flat=input("5.the world is flat: True or False?\n")
	i={
	"name" : name,
	"age" : age,
	"color" : color,
	"python" : python,
	"flat" : flat
	}
	print(f"hello {i['name']}, you said you are {i['age']} and you like {i['color']}.")
	if i["python"].lower()=="yes":
		print("you like python")
	else:
		print("you hate python")
	if i["flat"]=="True":
		print("you are dumb to think world is flat")
	else:
		print("you are smart to think world is not flat")

