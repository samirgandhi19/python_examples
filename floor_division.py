'''
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)
'''

'''
to get the rightmost digit of a number, you can modulo (%) the number by 10. To remove the rightmost digit you can floor divide (//) the number by 10. (Don't worry if you're not familiar with floor division—you can look up the documentation here. Remember, this is a challenge!)
'''

#this is a creative way to add together the individual numbers of an integer. 
def digit_sum(n):
  total = 0
  while n > 0:
    x = n % 10
    total += x
    n = n // 10
  return total

sum_num = int(raw_input("enter a positive number: "))
print digit_sum(sum_num)