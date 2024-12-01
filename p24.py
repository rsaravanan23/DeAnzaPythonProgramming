# p24.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that generates X random integers Num.

Num is a random number between 20 to 50. 

X is a random number between 10 to 15.

Calculate and show the Smallest, Largest, Sum, and Average of those numbers.
'''

from random import randint

x = randint(10,15)
print ("x =", x)
sum = 0
for i in range(0,x,1):
    number = randint(20,50)
    sum += number
    print(number, end=",")

    if i == 0:
        smallest = number
    else:
        if number < smallest:
            smallest = number

    if i == 0:
        largest = number
    else:
        if number > largest:
            largest = number
            
print()
print("Smallest:", smallest)
print("Sum:", sum)
print("Average: %.2f" %(sum/x) )
print("Largest:", largest)


'''
===================== RESTART: C:/Users/rishi/python/p24.py ====================
x = 13
36,29,20,35,24,43,23,44,45,31,40,44,36,
Smallest: 20
Sum: 450
Average: 34.62
Largest: 45

'''

