# p29.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
The absolute value of 1 is 1, and the absolute value of -1 is also 1.

Write a function that calculates the absolute value and returns the absolute value of a number.

Do not just use the built-in python function abs()! You must write the definition yourself!

Be sure to type the function name and the function calls below, copy/pasting it will give you errors!
'''

number = int(input("Please enter a postive or negative integer: "))

def absolute (number):
    if number >= 0:
        print("The absolute value of", number, "is", number)
    if number < 0:
        print("The absolute value of", number, "is", -1*number)

absolute(number)


'''

====== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p29.py ======
Please enter a postive or negative integer-4
The absolute value of -4 is 4

====== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p29.py ======
Please enter a postive or negative integer: 0
The absolute value of 0 is 0

====== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p29.py ======
Please enter a postive or negative integer: 3
The absolute value of 3 is 3

'''
