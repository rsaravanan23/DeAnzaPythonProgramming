# p12.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to determine if the user can vote. The program will ask the user a series of questions - age, citizenship and registration. The user will receive a message as to whether or not s/he may vote -- yes, no (with a reason - too young, not a citizen, hasn't registered to vote).

Be sure to test your program at least 4 times:

The user can vote
The user can't vote because they are not old enough.
The user can't vote because they are not old enough and not a citizen.
The user can't vote because they are not old enough, not a citizen, not registered.
Note: You must be over 18, registered , and a citizen to vote.

'''

age = int(input("Please enter age: "))
citizen = input("Are you citizen? (yes/no):").lower()
registered = input("Are you registered? (yes/no):").lower()

if age >= 18 and citizen == 'yes' and registered == 'yes':
    print('Congratulations, you can vote!')
else:
    if age < 18: 
        print("You are not old enough")
    if citizen != "yes":
        print("You are not a citizen")    
    if registered != "yes":
        print("You are not registered")    

''''

===================== RESTART: C:/Users/rishi/python/p12.py ====================
Please enter age: 19
Are you citizen? (yes/no):yes
Are you registered? (yes/no):yes
Congratulations, you can vote!

===================== RESTART: C:/Users/rishi/python/p12.py ====================
Please enter age: 17
Are you citizen? (yes/no):no
Are you registered? (yes/no):no
You are not old enough
You are not a citizen
You are not registered

===================== RESTART: C:/Users/rishi/python/p12.py ====================
Please enter age: 19
Are you citizen? (yes/no):no
Are you registered? (yes/no):yes
You are not a citizen

===================== RESTART: C:/Users/rishi/python/p12.py ====================
Please enter age: 19
Are you citizen? (yes/no):no
Are you registered? (yes/no):no
You are not a citizen
You are not registered

'''
