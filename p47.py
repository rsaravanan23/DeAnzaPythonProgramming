# p47.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program which :

Writes a random number (50 to 55) of numbers (0 to 100) in a file
Opens the file and reads the numbers from it into a list
Sorts the list (using Bubble Sort learned in this class) and Shows it.
Calculates the median.
Note: You may NOT use the Python built in functions: sort(), sorted(), sum(), median(), and can only use code you have learned in this class!
'''


#part 1

from random import randint

myFile = open('number.txt', 'w')

numOfNumbers = randint(50,55)
print ("numOfNumbers = ",numOfNumbers)
sum = 0
for i in range(0,numOfNumbers,1):
    number = randint(0,100)
    myFile.write(str(number) + '\n')
myFile.close()

myFile = open('number.txt', 'r')
numbersPerLineAsList = myFile.read().splitlines()


def sortList (value):
    
    for i in range (0,numOfNumbers,1):
        for j in range (0,numOfNumbers-1,1):
             if int(value[j]) > int(value[j+1]):
                 temp = value[j]
                 value[j] = value[j+1]
                 value[j+1] = temp
    print(value)
    
sortList(numbersPerLineAsList)



if  numOfNumbers % 2 != 0:
    median = int((numOfNumbers-1)/2 ) 
    print("Median =", numbersPerLineAsList[median])

   
   
if  numOfNumbers % 2 == 0:
    index1 = int(numOfNumbers/2 )
    index2 = int(numOfNumbers/2  - 1)
    median = (int(numbersPerLineAsList[index1]) + int(numbersPerLineAsList[index2])) / 2
    print("Median =", median)
    

'''

========================================================= RESTART: C:\Users\rishi\python\p47.py =========================================================
numOfNumbers =  55
['2', '5', '7', '8', '10', '11', '20', '20', '21', '24', '24', '24', '28', '31', '31', '32', '33', '33', '36', '38', '39', '40', '42', '43', '43', '46', '47', '48', '49', '57', '58', '59', '60', '62', '63', '65', '66', '68', '72', '73', '74', '75', '76', '77', '77', '79', '81', '84', '92', '92', '94', '94', '99', '100', '100']
Median = 48

========================================================= RESTART: C:\Users\rishi\python\p47.py =========================================================
numOfNumbers =  52
['2', '3', '11', '11', '14', '14', '16', '16', '21', '22', '24', '26', '27', '27', '32', '35', '36', '37', '39', '40', '43', '43', '44', '48', '49', '61', '62', '62', '66', '69', '70', '73', '75', '76', '78', '80', '80', '81', '82', '84', '85', '85', '87', '88', '91', '93', '95', '95', '96', '97', '98', '98']
Median = 61.5

'''
    
