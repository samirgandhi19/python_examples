#python cheetsheet

#Add to itself
cost = 30
cost += 20
''' cost now equals 50'''

# string methods
some_string = 'hello'
to_lowercase = some_string.lower()
to_uppercase = some_string.upper()
int_to_string = str(2)
string_to_int = int('99')
'''can also use float()
int() will round down floats'''
get_length = len(some_string)
''' can also get index of number like some_string[0]'''
'''can get part of a string like (some_string[1:len(some_string)])
this one gets all but the first letter'''

#index/list methods
some_list = ["one","two","three"]
len(some_list)
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

#dictionary methods
some_dictionary = {"one":"hello","two":"world","three":['I','am','sam']} #to create, key-values like JSON
del some_dictionary["one"] #to delete a key-value pair
some_dictionary["three"].remove('I')

#other methods
max(args) #max out of a list of numbers
min(args) #min out of a list of numbers
abs(arg)
print type(42) #returns <type 'int'>
#string printing
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

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

#import 
'''
import math #this requires you to still do math.sqrt(25)
from math import * #this imports all functions of math
**** its always best to either import module and type module.function or 
import specific variables and funcrtions ****
'''