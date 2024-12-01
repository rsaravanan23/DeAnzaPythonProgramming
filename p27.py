# p27.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that generates a random list of letters.

# start with an
empty_list = [ ]
# and use
empty_list.append(Letter) # to add letters to the list

The length of the list of letters changes every time you run the program.

There can be a random number of X  letters on the list, where X is a random number between 50 to 75.

Each of the letters on the list is a random letter between A to F (uppercase).

Use a loop to generate the list and then Show the generated list of letters to the user.

Count and then show to the user how many times the letter B appears.

In order to receive credit, you may not use python built-in function "count()" !

'''

from random import randint

count = 0
x = randint(50,75)
empty_list = [ ]

for y in range(0,x,1):
    asciiNumber = randint(65,70)
    empty_list.append(chr(asciiNumber))
    if asciiNumber == 66:
        count += 1

print ("Here is a list with", x, "letters: ")
print()
print (empty_list)
print()
print ("The letter 'B' appears", count, "times")


'''

= RESTART: C:\Users\rishi\python\p27.py
Here is a list with 69 letters: 

['A', 'D', 'F', 'D', 'D', 'A', 'C', 'C', 'E', 'D', 'E', 'F', 'D', 'B', 'C', 'A', 'C', 'C', 'D', 'F', 'B', 'F', 'C', 'D', 'B', 'F', 'A', 'C', 'A', 'F', 'D', 'D', 'A', 'A', 'A', 'B', 'D', 'B', 'A', 'A', 'D', 'D', 'A', 'B', 'A', 'B', 'A', 'A', 'F', 'D', 'F', 'F', 'F', 'C', 'A', 'C', 'A', 'A', 'E', 'F', 'B', 'D', 'E', 'E', 'B', 'B', 'C', 'A', 'E']

The letter 'B' appears 10 times

'''
