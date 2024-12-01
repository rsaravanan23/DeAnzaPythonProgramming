# p30.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''

Write a function which has two parameters, N and M.

The function returns True if N is evenly divisible by M, and False otherwise.

Be sure to type the function name and the function calls below, copy/pasting it will give you errors!
'''

def isDivisible (N,M):
    if N%M == 0:
        return True
    if N%M != 0:
        return False

print(isDivisible(8,4))
print(isDivisible(9,5))


'''

====== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p30.py ======
True
False

'''
