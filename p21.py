# p21.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Which of the below gives you more money?

1) A penny which doubles it's value every day over 30 days, or

2) A million dollars

Write a program which calculates exactly how much more (or less) you can make with the penny on day 30. A loop must be used.
'''

dollars = 1000000
pennies = 0.01
for days in range (1,31,1):
    pennies = pennies * 2
    print("pennies : " + str(pennies))

print("Pennies %.2f Dollares %i" %(pennies, dollars))


'''

===================== RESTART: C:\Users\rishi\python\p21.py ====================
pennies : 0.02
pennies : 0.04
pennies : 0.08
pennies : 0.16
pennies : 0.32
pennies : 0.64
pennies : 1.28
pennies : 2.56
pennies : 5.12
pennies : 10.24
pennies : 20.48
pennies : 40.96
pennies : 81.92
pennies : 163.84
pennies : 327.68
pennies : 655.36
pennies : 1310.72
pennies : 2621.44
pennies : 5242.88
pennies : 10485.76
pennies : 20971.52
pennies : 41943.04
pennies : 83886.08
pennies : 167772.16
pennies : 335544.32
pennies : 671088.64
pennies : 1342177.28
pennies : 2684354.56
pennies : 5368709.12
pennies : 10737418.24
Pennies 10737418.24 Dollares 1000000

'''
