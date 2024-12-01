# p23.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to let a child practice arithmetic skills.

The program should first ask for what kind of practice is wanted: addition(1), subtraction(2), or multiplicatio(3)... (no division).

Then, the program will have a loop for each of the the desired operations that lets the user repeat the practice as many times as desired,

Two random numbers will be generated (0 - 9), and the child will have to add, subtract or multiply them.

If the child answers the question correctly, congratulate them, and give them two different numbers to try.

If the child answers incorrectly, the problem should be repeated (with the two same numbers).

Note: You are not allowed to use the eval() or sum() functions!


'''
from random import randint

while True:
    x = int(input("Would you like to add(1), subtract (2) or multiply(3)"))

    num1 = randint(0,9)
    num2 = randint(0,9)
    
    if x < 1 or x > 3:
        incorrect = input("Please enter a number between 1 and 3: ") 
    if x == 1:
        addition = int(input("What is %i + %i equal to: " %(num1,num2)))
        while addition != num1+num2:
            addition = int(input("Incorrect,what is %i + %i equal to: " %(num1,num2)) )
    if x == 2:
        subtraction = int(input("What is %i - %i equal to: " %(num1,num2)))
        while subtraction != num1-num2:
            subtraction = int(input("Incorrect,what is %i - %i equal to: " %(num1,num2)) )
    if x == 3:
        multiplication = int(input("What is %i * %i equal to:" %(num1,num2)))
        while multiplication != num1*num2:
            multiplication = int(input("Incorrect,what is %i * %i equal to:" %(num1,num2)) )


    again = input("Do you want to try again (yes/no): ")
    if again != "yes":
        break

























