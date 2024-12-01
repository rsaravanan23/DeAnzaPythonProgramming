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


def sum(listA):
    sumOfList = 0
    for index in range(0,len(listA),1):
        sumOfList = sumOfList + listA[index]
    return sumOfList

def average(listB):
    totalSum = sum(listB)
    avg = totalSum / len(listB)
    return avg

def min(listC):
    smallest = listC[0] 
    for i in range(1,len(listC),1):
        if listC[i] < smallest: 
           smallest = listC[i]
    return smallest

def max(listD):
    largest = listD[0] 
    for i in range(1,len(listD),1):
        if listD[i] > largest: 
           largest = listD[i]
    return largest

def main():
    numList = [1,2,3,5,7]

    sumMain = sum(numList)
    averageMain = average(numList)
    minMain = min(numList)
    maxMain = max(numList)
    print("The sum is", sumMain)
    print("The avg is", averageMain)
    print("The min is", minMain)
    print("The max is", maxMain)

main()


'''

======= RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p42.py ======
The sum is 18
The avg is 3.6
The min is 1
The max is 7

'''
