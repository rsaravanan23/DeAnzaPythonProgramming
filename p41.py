# p41.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a function which outputs as many crosses
as the parameter 'numCrosses' indicates.

def stars(numCrosses):
For example, when parameter 'numCrosses' equals 5,
the function displays the following:

+ 
+ + 
+ + + 
+ + + + 
+ + + + +
You are not allowed to use string "concatenation" or multiplication.
Also the use of a list and appending to a list is not permitted.
You must solve the problem using 2 loops (one 'for' loop nested in the other).
'''

def stars(numCrosses):

    for rowNum in range(0, numCrosses, 1):
       print (" * ", end= ' ')
       for i in range (0, rowNum, 1): 
          print (" * ",end = ' ' )

       print ( )                   

stars(6)

'''

======================= RESTART: C:\Users\rishi\python\p41.py =======================
 *  
 *   *  
 *   *   *  
 *   *   *   *  
 *   *   *   *   *  
 *   *   *   *   *   *  

'''
