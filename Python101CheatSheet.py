#!/bin/python3

#Print string
print("Strings and things:")
print('Hello, World')
print("""Hello, this is 
a multi-line string!""")
print("This is"+" a string")

print('\n') #new line

#Math 
print("Math time:")
print(50 + 50) #Add
print(50 - 50) #subtract
print(50 * 50) #Multiply
print(50 / 50) #Divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers

print('\n') #new line

#Variables & Methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title


name = "Clay"
age = 22 #int int(22)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(22.9)) #Integer doesnt round it cuts off the decimal

print("My name is " + name + " and I am " + str(age) + " years old.")
print('\n') #new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions
print("Now, some functions:")
def who_am_i():
	name1 = "Clay"
	age = 22
	print("My name is " + name1 + " and I am " + str(age) + " years old.")
who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x + y)
	
add(7,7)
add(305,207)

#Using return
def multiply(x,y):
	return x * y
print(multiply(7,7))

def square_root(x):
	return x ** .5
print(square_root(64))

print('\n') #new line

#Boolean expressions (True or False)
print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and= (7 > 5) and (6 < 7)
test_or= (7 > 5) or (5 < 7)
test_not= not True

print(test_and)

print('\n') #new line

#Conditional Statements
print("Conditional Statements:")
def soda(money):
	if money >= 2:
		return "Youve got yourself a soda!"
	else:
		return "No soda for you pal"
print(soda(3))
print(soda(1))


def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We getttin litty on foenem"
	elif (age >= 21) and (money <5):
		return "Come back with more bread"
	elif (age < 21) and (money >= 5):
		return "Nice try kid"
	elif (age < 21) and (money <5):
		return "Youre too poor and young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

print('\n') #new line

#Lists
print("Lists have brackets:")
movies = ["21 Jump Street", "Bad Boys", "Superbad", "Step Brothers"]

print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop() #Removes last item in list
print(movies)

movies.pop(1)
print(movies)

movies = ["21 Jump Street", "Bad Boys", "Superbad", "Step Brothers"]
person = ["Clay", "Mom", "Victoria", "Dad"]
combined = zip(movies, person) #combines
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "Spinach", "cabbage"]
for x in vegetables:
	print(x)
	
print("While loops - Execute as long as True:")
i = 1
while i < 10:
	print(i)
	i += 1
