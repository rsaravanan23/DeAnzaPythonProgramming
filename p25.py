# p25.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that asks the user to input a sentence.

The program will ask the user what two letters are to be counted.

You must use a “for” loop to go through the sentence & count how many times the chosen letter appears in the sentence.

You are not allowed to use python built-in function "count()" or you'll get a Zero!

Output will show the sentence, the letter, and the number of times the letter appears in the sentence.operator = int(input 
'''
x = input("Input a sentence: ")
count_one = 0
count_two = 0

letter_one  = input("Please enter letter 1: ")
letter_two  = input("Please enter letter 2: ")

for index in range (0,len(x), 1):
    if (x[index] == letter_one):
        count_one += 1
    if (x[index] == letter_two):
        count_two += 1

print("The letter" , letter_one, "was found", count_one, "times")
print("The letter" , letter_two, "was found", count_two, "times")

'''

===================== RESTART: C:/Users/rishi/python/p23.py ====================
Input a sentence: hello world
Please enter letter 1: o
Please enter letter 2: f
The letter o was found 2 times
The letter f was found 0 times

'''
