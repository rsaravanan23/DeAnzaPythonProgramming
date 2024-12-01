# p31.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a function that has an integer N as parameter and returns true if N is even.

Hint: A number N is even if N % 2  == 0

Be sure to type the function name and the function calls below, copy/pasting it will give you errors!
'''

def isDivisible (N):
    if N%2 == 0:
        return True
    if N%2 != 0:
        return False

print(isDivisible(10))
print(isDivisible(7))


'''

====== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p31.py ======
True
False

'''
