# p28.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a function which given two integer parameters Returns their sum...unless the two values are the same, then the function Returns their doubled sum.

Be sure to type the function name and the function calls below, copy/pasting it will give you errors!
'''

def sum (x,y):
    if x == y:
        doubleXY = 2*(x+y)
        return doubleXY
    if x != y:
        return x + y


print("If both numbers are different then the sum is",sum(4,7))
print("If both numbers are the same then double the sum is",sum(3,3))


'''
===================== RESTART: C:\Users\rishi\python\p28.py ====================
If both numbers are different then the sum is 11
If both numbers are the same then double the sum is 12

'''
