# p13.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to convert any given number of total cents (under 100) into the correct number of: quarters, dimes, nickels, pennies.

'''

total_cents = int(input('Enter total number of cents:'))

quarters = int(total_cents/25)
if quarters > 0: 
    print ("Quarters: ", quarters)
    total_cents = total_cents - quarters*25

dimes = int(total_cents/10)
if dimes > 0:
    print ("Dimes: ", dimes)
    total_cents = total_cents - dimes*10 

nickles = int(total_cents/5)
if nickles > 0:
    print ("Nickles: ", nickles)
    total_cents = total_cents - nickles*5

pennies = int(total_cents/1)
if pennies > 0:
    print ("Pennies: ", pennies)
    total_cents = total_cents - pennies*1

'''

===================== RESTART: C:/Users/rishi/python/p13.py ====================
Enter total number of cents:66
Quarters:  2
Dimes:  1
Nickles:  1
Pennies:  1

===================== RESTART: C:/Users/rishi/python/p13.py ====================
Enter total number of cents:16
Dimes:  1
Nickles:  1
Pennies:  1

===================== RESTART: C:/Users/rishi/python/p13.py ====================
Enter total number of cents:6
Nickles:  1
Pennies:  1

===================== RESTART: C:/Users/rishi/python/p13.py ====================
Enter total number of cents:4
Pennies:  4

'''
