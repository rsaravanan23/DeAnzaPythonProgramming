# p22.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a Dice Game program that generates two random dice values between 1 and 6 for you, and 2 for the computer.

You get to roll as many times as you like (if you don't like your 2 dice), while the computer only rolls once, after you
have decided that you like your two dice. 

Determine who wins, you or the computer.
'''

from random import randint
while True:
    player1 = randint(1,6)
    player2 = randint(1,6)
    playerTotal = player1 + player2
    change = input("You have %i and %i which equals to %i. Do you want to change these numbers (y/n)" %(player1,player2,playerTotal))
    if change == 'n':
        break
print()

computer1 = randint(1,6)
computer2 = randint(1,6)
computerTotal = computer1 + computer2
print("Computer values were:", computer1, "and",computer2, "which equals", computerTotal)
print()


if playerTotal > computerTotal:
    print("Players wins")
elif playerTotal < computerTotal:
    print("Computer wins")
else:
    print("It's a tie")

'''

===================== RESTART: C:\Users\rishi\python\p22.py ====================
You have 1 and 5 which equals to 6. Do you want to change these numbers (y/n)y
You have 4 and 3 which equals to 7. Do you want to change these numbers (y/n)n

Computer values were: 4 and 2 which equals 6

Players wins

'''
