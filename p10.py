# p10.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program which asks the user for a student's grade as a percent, and then returns their letter grade.

Validate the input to make sure that the number is between 0 - 100 . If for any other number, say "ERROR" and ask for another number)

A is 90% or above
B is between 80% and 90%
C is between 70% and 80%
D is between 60% and 70%
F is under 60%

Sample Run:
    Please enter a grade in percent: -1
    Error, the number must be between 0 to 100.
    Please enter a grade in percent: 75
    You have a "C"

'''

grade = float(input("Please enter a grade as a percent:"))

if grade < 0 or grade > 100:
    print("Invalid, grade must be between 0 to 100")
    grade = float(input("Please enter a grade as a percent:"))
elif grade >= 90 and grade <= 100:
    print("The grade is an A")
elif grade >= 80 and grade <= 90:
    print("The grade is a B")
elif grade >= 70 and grade <= 80:
    print("The grade is a C")
elif grade >= 60 and grade <= 70:
    print("The grade is a D")
elif grade >= 0 and grade <= 60:
    print("The grade is a F")

'''

===================== RESTART: C:/Users/rishi/python/p10.py ====================
Please enter a grade as a  percent:95
The grade is an A

'''
