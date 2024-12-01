# p9.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to compute a person's height and print out a message.

The user will input their height in feet and inches.

The program will convert the feet and inches into total_inches, and then print a message.

If the total inches is greater than 72, the message should be something like, "You're tall."
If the total inches is between 5' and 6', a different message should appear, like "You are average"
If the total inches is less than 60, another message should appear, like "You are vertically challenged"
'''

feet = int(input("Please enter the number of feet:"))
inches = int(input("Please enter the number of inches:"))

if feet < 0 or inches < 0:
    print("This is an invalid height")
else:   
    total_inches = feet*12 + inches
    
    if total_inches > 72:
        print ("You're tall")
    elif total_inches < 72 and total_inches > 60:
        print ("You're average")
    elif total_inches < 60 and total_inches > 0:
        print ("You're vertically challenged")    


#===================== RESTART: C:\Users\rishi\python\p9.py =====================
#Please enter the number of feet:5
#Please enter the number of inches:3
#You're average
