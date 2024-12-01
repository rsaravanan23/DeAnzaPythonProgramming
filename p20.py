# p20.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that reads in X whole numbers and outputs (1) the sum of all positive numbers, (2) the sum of all negative numbers,
and (3) the sum of all positive and negative numbers. The user can enter the X numbers in any different order every time, and can
repeat the program if desired. 

'''

while True:

    x = int(input("Enter a whole number: "))
    sumAll = 0
    sumNeg = 0
    sumPos = 0

    for k in range (0,x,1):
        num = int(input("Enter number %i: " %(k+1)))
        sumAll = sumAll + num
        if num < 0:
            sumNeg = sumNeg + num
        if num > 0:
            sumPos = sumPos + num
    print("Total sum:", sumAll)
    print("Positive sum:", sumPos)
    print("Negative Sum:", sumNeg)
    
    repeat = input("Would you like to repeat this program (y/n)")
    if repeat != 'y':
        break

'''

==================== RESTART: C:\Users\rishi\python\p20.py ====================
Enter a whole number: 3
Enter number 1: 2
Enter number 2: 5
Enter number 3: -4
Total sum: 3
Positive sum: 7
Negative Sum: -4
Would you like to repeat this program (y/n)y
Enter a whole number: 2
Enter number 1: -3
Enter number 2: 4
Total sum: 1
Positive sum: 4
Negative Sum: -3
Would you like to repeat this program (y/n)n

'''

