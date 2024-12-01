# p3.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Type up the Example input.py program below, including the comments, and get it working.
When the program runs, copy/paste the Output (in BLUE) at the bottom of your program as a multi-line comment '''     ''', then save the file.
Submit input.py
'''

name = input("Please enter your name: ") # this is a string
weightLbs = float(input("Please enter your weight in lbs: ")) # a float
age = int(input("Please enter your age (whole number): ")) # an integer
weightKg = weightLbs*0.453592
title = "Human"

print("Hello", title, name, "your weight is")
print(weightLbs , "lbs")
print("which equals = %.2f" %weightKg, end=' ') # end = ' ' prevents new line
print ("kilograms ")

'''

===================== RESTART: C:/Users/rishi/python/p3.py =====================
Please enter your name: Rishi
Please enter your weight in lbs: 108
Please enter your age (whole number): 15
Hello Human Rishi your weight is
108.0 lbs
which equals = 48.99 kilograms 

'''
