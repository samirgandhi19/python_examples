functions_list = []
'''
this small program is to show case some math and other functions. 
'''

#=====================================================================
#floor_division
'''
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)
'''

'''
'''

#this is a creative way to add together the individual numbers of an integer. 
def digit_sum(n):
	total = 0
	while n > 0:
		x = n % 10
		total += x
		n = n // 10
	return total
functions_list.append("digit_sum")
#=====================================================================

#=====================================================================
#factorial
'''
factorial means taking a number and multiplying it by every number less than it. 
this function is a cool way to accomplish it by calling itself. 
'''
def factorial(x):
	if x == 1:
		return 1
	else:
		return x*factorial(x-1)
print factorial(6)
functions_list.append("factorial")

#=====================================================================

#=====================================================================
#is_prime
def is_prime(x):
	prime = True
	if x in (0,1) or x < 0:
		return False
	else:
		for n in range(2,x-1):
			if (x % n) == 0:
				prime = False
				break
	return prime
functions_list.append("is_prime")
#=====================================================================

#=====================================================================
#reverse_text
def reverse_text(text):
		word = ""
		l = len(text) - 1
		while l >= 0:
				word = word + text[l]
				l -= 1
		return word
functions_list.append("reverse_text")
#=====================================================================

#=====================================================================

def anti_vowel(text):
	back = ""
	for char in text:
		if char not in ["a","e","i","o","u","A","E","I","O","U"]:
			back += char
	return back  
functions_list.append("anti_vowel")

#=====================================================================

#=====================================================================

def censor(text, word):
	sentence = ""
	text_list = text.split(" ")
	for index, item in enumerate(text_list):
		if item == word:
			text_list[index] = "*" * len(item)
		else: sentence += item
		sentence = " ".join(text_list)
	print sentence
	return sentence

#=====================================================================


choose_func = 'y'
while choose_func == 'y':
	print "welcome, let's explore some math functions... choose a function from: ", functions_list
	func = raw_input(": ")
	if func == 'digit_sum':
		print digit_sum(int(raw_input("enter a positive number: ")))
	elif func == 'factorial':
		print factorial(int(raw_input("enter a positive number (small is a good idea): ")))
	elif func == 'is_prime':
		print is_prime(int(raw_input("enter a number: ")))
	elif func == 'reverse_text':
		print reverse_text(raw_input("enter some text: "))
	elif func == 'anti_vowel':
		print anti_vowel(raw_input("enter some text: "))
	elif func == 'censor':
		print censor(raw_input("enter some text:"),raw_input("enter word to censor: "))
	choose_func = raw_input("would you like to try another?: (y/n)")
else:
	print "goodbye"