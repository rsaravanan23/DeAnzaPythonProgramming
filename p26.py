# p26.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that generates a random list of numbers.

(start with an empty list and use append() )

The length of the list X can be a random number between 15 to 20.

Each of the random numbers on the list can be between 2 to 5.

Count how many times the number 3 appears.

Sample: generating a list of 18 numbers
[5, 5, 4, 2, 3, 5, 4, 3, 2, 5, 3, 2, 5, 3, 5, 3, 2, 2]
The number 3 occurs 5 times
'''

from random import randint

x = randint(15,20)
print("Generating a list of", x , "numbers")
emptyList = []
for i in range (0,x,1):
    emptyList.append(randint(2,5))
print(emptyList," ", end = "")
print()

count = 0
num_three = 3
for index in range (0,x,1):
    if (emptyList[index] == num_three):
        count += 1

print("The number 3 was found", num_three , "times")

'''

===================== RESTART: C:\Users\rishi\python\p26.py ====================
Generating a list of 15 numbers
[4, 2, 5, 2, 2, 4, 3, 2, 4, 2, 4, 4, 5, 5, 5]  
The number 3 was found 3 times

'''
