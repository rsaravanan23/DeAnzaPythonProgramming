# p14.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that asks the user to enter 4 numbers (positive or negative).

The program shows:

the sum of all numbers (sumAll)
the sum of positive numbers (sumPos),
the sum of negative numbers (sumNeg)
The Algorithm for this problem:

sumNeg is going to hold the total of all negative numbers, it starts at zero (0)
sumPos is going to hold the total of all positive numbers, it starts at zero (0)
if a number is negative you ADD it to sumNeg
if a number is positive you ADD it to sumPos
'''

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))

sum_all = 0
sum_all = a+b+c+d
print("Sum_all:", sum_all)


sum_neg = 0
if a < 0:
    sum_neg += a 
if b < 0:
    sum_neg += b
if c < 0:
    sum_neg += c
if d < 0:
    sum_neg += d
print("Sum_neg:", sum_neg)

sum_pos = 0
if a > 0:
    sum_pos += a 
if b > 0:
    sum_pos += b
if c > 0:
    sum_pos += c
if d > 0:
    sum_pos += d
print("Sum_pos:", sum_pos)

'''
===================== RESTART: C:/Users/rishi/python/p15.py ====================
Enter number 1: 3
Enter number 2: 5
Enter number 3: -2
Enter number 4: -3
Sum_all: 3.0
Sum_neg: -5.0
Sum_pos: 8.0

'''


