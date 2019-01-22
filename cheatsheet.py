#python cheetsheet

#Add to itself
cost = 30
cost += 20
i = 10 #sets i to 10
i == 10 #compares if i is 10. returns true
''' cost now equals 50'''
#comparison and math
print 2+2 # 2
print 3-1 # 2
print 1*2 # 2
print 4/2 # 2
print 5/2 # 2 
'''this last one is tricky, it always rounds down. 
EVEN IF you convert to a float. 
if you want the ACTUAL number, divide by a FLOAT
'''

# string methods
some_string = 'hello'
to_lowercase = some_string.lower()
to_uppercase = some_string.upper()
int_to_string = str(2)
string_to_int = int('99')
'''can also use float()
int() will round down floats'''
get_length = len(some_string)
''' can also get item by index like some_string[0]'''
'''can get part of a string like (some_string[1:len(some_string)])
this one gets all but the first letter'''
#string printing
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h) #prints Golf, Hotel
print g, ", ",h #prints Golf, Hotel
some_list.split("")



#index/list methods
some_list = ["one","two","three"]
len(some_list) #returns number of items in list
some_list.append("four") #adds to end of list
some_list.index("one") #returns 0
some_list.insert(0,"zero") #some_list now =["zeo",one","two","three"]
for item in some_list:
	print(item) #this is like a JS forEach loop
some_list.sort() #sorts strings alphabetically, and numbers least-most
some_list.remove("three") #must be item in list
some_list.pop(1) #removes and returns item at this index
del(some_list[1]) #removes index but doesn't return
#range(start, stop, step)
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4] 
'''lists can be added together'''
''' you can also iterate through a list of lists twice to
 get down to the individual elements'''
d = {"name": "Eric","age": 26}
for key in d:
  print key, d[key]
for letter in "Eric":
  print letter,  # note the comma! prints all next to each other

#List Comprehenshion
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

#List Slicing [start:end:stride]
to_one_hundred = range(1,101)
backwards_by_ten = to_one_hundred[1:100:-10]

#Lambda (annonymous functions)
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)

#List comp + Lambda: 
squares = [x**2 for x in range(1,11)]
print filter(lambda i: i >30 and i <70,squares)

#dictionary methods
some_dictionary = {"one":"hello","two":"world","three":['I','am','sam']} #to create, key-values like JSON
del some_dictionary["one"] #to delete a key-value pair
some_dictionary["three"].remove('I')

#other methods
max(args) #max out of a list of numbers
min(args) #min out of a list of numbers
abs(arg)
print type(42) #returns <type 'int'>

#dates
from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day

#conditional + function
num = raw_input("enter a number: ")
'''define a function to compare entry vs 5'''
def check_num(number):
	if number <= 5:
		print str(num) + 'is less than or equal to 5'
	elif number > 5:
		print str(num) + ' is greater than 5'
'''check if entry is valid integer, then call function'''
if num.isalpha():
	print 'please use an integer'
else:
	num = int(num)
	check_num(num)
if "d" in "dog":
	print "yes!"
if "d" not in ["d","o","g"]:
	print 'Nope!'
#Loops
'''for loops work more like forEach loops in JS'''
for i in range(5):
	print i #prints 0 1 2 3 4
'''strings are stored in variables as lists, so you can even do'''
word = "hello"
for letter in word:
	print letter #prints h e l l o
'''While loops are more commonly used'''
x = 1
while x <= 10:
	print x
	x += 1 #prints 1 2 3 4 5 6 7 8 9 10
else:
	print "done!"
'''while loops in python can have an else after the loop, 
this will be executed if the loop is falsified, 
not if the loop breaks
'''
'''use enumerate with for loop to know iteration of loop'''
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1,item 
'''prints: 
Your choices are:
1 pizza
2 pasta
3 salad
4 nachos
'''

#import 
'''
import math #this requires you to still do math.sqrt(25)
from math import * #this imports all functions of math
**** its always best to either import module and type module.function or 
import specific variables and funcrtions ****
'''

#binary = base 10
print 0b1111 # 15
print int("111",2) # 7 - this converts the string to base 10
print int("0b100",2) # 4 converts to base 
print bin(0b10111011 | 0b100) #0b1011111
# & - returns which bits are on in BOTH
# | returns where bits are on in either
# ^ returns where bits are on in either but not both. Useful for flipping a whoele bit
# masks are just variables that you will use to convert bits. 

#Object-Oriented Programming
'''
create base class'''
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
  	''' __init__ is proper way to construct the object attributes, 
  	self should be the first thing passed'''
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  '''this is overriding a obj method'''
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  '''call the parent function from child with super'''  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

#writing files: 
my_file = open("somefile.txt","w") #opens file in write mode
my_file.write("Hello, I'm Samir")
my_file.close() #ALWAYS CLOSE FILES
my_file.closed #true or false if file is closed
'''quick way to run something on a file and auto close'''
with open("text.txt","w") as my_file:
	my_file.write("Success!")

#Additional Notes!
'''
getting used to python syntax is interesting. will need to stay in practice
use the cheatsheet to remember differences between classes, methods, etc
'''

