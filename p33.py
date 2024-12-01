# p33.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the
other two are one inch long, you will not be able to get the short sticks to meet in the middle.

For any three sticks, there is a simple test to see if it is possible to form a triangle:

“If any of the three sticks is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can.”

Write a function named isTriangle(a,b,c) that has three sides a,b,c  as parameters.

The function returns either True or False, depending on whether you can form a triangle from the sides with the given lengths.
'''

def isTriangle(a,b,c):
    
    if a+b >= c and b+c >= a and a+c >= b:
        print("This is a triangle: True")
    else:
        print("This is a triangle: False")


isTriangle(4,5,6)
isTriangle(15,5,6)


'''

===================== RESTART: C:\Users\rishi\python\p33.py ====================
This is a triangle: True
This is a triangle: False

'''
