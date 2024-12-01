# p51.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
1) Create a Date class.

1a) The class should have 3 properties (instance variables):

month
day
year
1b) The class should have 2 actions (functions / methods) :

setDate()  - allows the user to enter a date in 12/31/02 format 
showDate() - displays the date. 
2) Create an instance of the Date class.

3) Test the object's setDate() and showDate() methods.
'''

class hello:

    def __init__(self, newMonth=0, newDay=0, newYear=0):
        self.month = newMonth
        self.day = newDay
        self.year = newYear

    def setDate(self):
        userDate = input("Please enter a date in this format(month/day/year): ")
        s = userDate.split('/')
        self.month = int(s[0])
        self.day = int(s[1])
        self.year = int(s[2])

    def showDate(self):
        print(str(self.month) + '/' + str(self.day) + '/' + str(self.year))


date = hello()

date.setDate()
date.showDate()



        
