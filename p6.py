# p6.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to compute a person's height.

INPUT: User will enter two whole numbers: feet and inches.
OUTPUT: Values input & total in inches.
INPUT VALIDATION: Make sure that feet and inches are positive values
Your program must run as shown below:

Please enter the number of feet:  4
Please enter the number of inches:  10
4 feet 10 inch(es) = 58 inches
'''

feet = int(input("Please enter the number of feet:"))
inches = int(input("Please enter the number of inches:"))

if feet < 0:
    print("This is an invalid height")

elif inches < 0:
    print("This is an invalid height")

else:
    total_inches = feet*12 + inches
    print(feet, "feet", inches, "inch(es) =", total_inches, "inches")


'''

===================== RESTART: C:/Users/rishi/python/p6.py =====================
Please enter the number of feet:5
Please enter the number of inches:4
5 feet 4 inch(es) = 64 inches

'''


