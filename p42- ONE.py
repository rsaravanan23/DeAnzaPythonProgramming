# p42.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write the below 5 functions according to the following requirements:

sum (list_parameter) : returns the sum of numbers inside a list
average (list_parameter) : returns the average of numbers inside a list
min (list_parameter) : returns the smallest of all numbers inside a list
max (list_parameter) : returns the largest of all numbers inside a list
main () : calls all the other functions above
'''
numList = [1,2,3,5,7]


def sum():
    sumOfList = 0
    for index in range(0,len(numList),1):
        sumOfList = sumOfList + numList[index]
    return sumOfList

def average():
    totalSum = sum()
    avg = totalSum / len(numList)
    return avg

def min():
    smallest = numList[0] 
    for i in range(1,len(numList),1):
        if numList[i] < smallest: 
           smallest = numList[i]
    return smallest

def max():
    largest = numList[0] 
    for i in range(1,len(numList),1):
        if numList[i] > largest: 
           largest = numList[i]
    return largest

def main():
    sumMain = sum()
    averageMain = average()
    minMain = min()
    maxMain = max()
    print("The sum is", sumMain)
    print("The avg is", averageMain)
    print("The min is", minMain)
    print("The max is", maxMain)

main()


