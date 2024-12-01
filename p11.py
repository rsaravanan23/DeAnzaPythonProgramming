# p11.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program to simulate rock-paper-scissors game.

Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.

The program then shows the winner on the basis of:

Paper covers Rock
Rock breack Scissors
Scissors cut Paper
Tie
Test your program multiple times to makes sure it works! Submit all 4 of your tests as a comment.
'''

p1 = int(input("player1 please enter 1 for rock, 2 for paper, 3 for scissors:"))
p2 = int(input("player2 please enter 1 for rock, 2 for paper, 3 for scissors:"))

rock = 1
paper = 2
scissors = 3

print("player1:", p1)
print("player2:", p2)

#if p1 wins
if p1 == rock and p2 == scissors:
    print("player1 wins since rock breaks scissors")
elif p1 == paper and p2 == rock:
    print("player1 wins since paper covers rock")
elif p1 == scissors and p2 == paper:
    print ("player1 wins since scissors cut paper")

#if p2 wins
if p2 == rock and p1 == scissors:
    print("player2 wins since rock breaks scissors")
elif p2 == paper and p1 == rock:
    print("player2 wins since paper covers rock")
elif p2 == scissors and p1 == paper:
    print ("player2 wins since scissors cut paper")

#if its a tie
if p1 == rock and p2 == rock:
    print("It's a tie")
elif p1 == paper and p2 == paper:
    print(" It's a tie")
elif p1 == scissors and p2 == scissors:
    print("It's a tie")

'''

===================== RESTART: C:/Users/rishi/python/p11.py ====================
p1 please enter 1 for rock, 2 for paper, 3 for scissors:2
p2 please enter 1 for rock, 2 for paper, 3 for scissors:3
p1: 2
p2: 3
p2 wins since scissors cut paper

===================== RESTART: C:/Users/rishi/python/p11.py ====================
p1 please enter 1 for rock, 2 for paper, 3 for scissors:1
p2 please enter 1 for rock, 2 for paper, 3 for scissors:2
p1: 1
p2: 2
p2 wins since paper covers rock

===================== RESTART: C:/Users/rishi/python/p11.py ====================
p1 please enter 1 for rock, 2 for paper, 3 for scissors:1
p2 please enter 1 for rock, 2 for paper, 3 for scissors:3
p1: 1
p2: 3
p1 wins since rock breaks scissors

===================== RESTART: C:/Users/rishi/python/p11.py ====================
p1 please enter 1 for rock, 2 for paper, 3 for scissors:2
p2 please enter 1 for rock, 2 for paper, 3 for scissors:2
p1: 2
p2: 2
It's a tie

'''


