# p7.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Circumference & Area of a Circle
    Write a program to compute the circumference and area of a circle.
    The user will input the radius of a circle.
    Validate Input: Make sure that the radius is positive, or give an error message.
    The program will show the circumference and area of a circle with that radius.
    The answers should be rounded to the nearest tenth.
Program should run as shown:
    What is the radius (in inches) of the circle you want to draw?  12
    A circle with radius 12 inches has
    circumference:   75.4 inches
    area:   452.4 sq. inches
Algorithm
    Use 3.1415 as the value of PI.
    Enter radius
    Circumference of a Circle = 2 * PI * R
    Area of a Circle = PI * R*R
'''

PI = 3.1415
radius = float(input("What is the radius (in inches) of the circle you want to draw?"))


if radius < 0:
  print("Radius cannot be negative")
else:
    area = PI*radius*radius
    circumference = 2*PI*radius
    print('A circle with the radius %.1f inches has' %radius)
    print('circumference: %.1f inches' %circumference)
    print('area: %.1f inches' %area)

'''

===================== RESTART: C:/Users/rishi/python/p7.py =====================
What is the radius (in inches) of the circle you want to draw?3
A circle with the radius 3.0 inches has
circumference: 18.8 inches
area: 28.3 inches

'''
    
