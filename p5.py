# p5.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program which computes the sum and product of two numbers entered by the user.

Algorithm:
Ask the user to enter two numbers.
store those two numbers in 2 variables, num1, num2.
make two new variables sum = num1+ num2, and product = num1*num2
Then, output the sum and product of to the user.
Sample Program Run:
Please enter number 1: 10

Please enter number 2: 20

The sum of 10 and 20 is 30

The product of 10 and 20 is 200
'''

#enter values:
num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))

#calculate:
sum = num1 + num2 # sum of two numbers
product = num1*num2 # product of two numbers

#results:
print("The sum of ", num1, "and ", num2, "is ", sum) 
print("The product of ", num1, "and ", num2, "is ", product) 

'''

======================= RESTART: C:/Users/rishi/python/p5.py ======================
Please enter first number:2
Please enter second number:5
The sum of  2 and  5 is  7
The product of  2 and  5 is  10

'''

