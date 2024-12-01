# p40.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Ask the user to enter X numbers into a list. Calculate and show the sum, average, min, max of those numbers.

Note: You are not allowed to use any pre-existing python functions such as sample(), sum(), min(), max(), average(), sort(), sorted()!!!...unless
you write them yourself.

'''
length = int(input("How many numbers would you like to enter? "))

numList = []
for a in range(0,length,1):
    num = int(input("Please enter number %i : " %(a + 1 ) ) )
    numList.append(num)
    
print('List =', numList) 

    

smallest = numList[0]
sumOfList = numList[0] 
for b in range(1,len(numList),1):
    if numList[b] < smallest: 
           smallest = numList[b]
    sumOfList = sumOfList + numList[b]
    
print("The sum is", sumOfList)
print('The min is', smallest)



avg = sumOfList / len(numList)
print("The avg is %.2f" %avg)


'''

======================= RESTART: C:\Users\rishi\python\p40.py =======================
How many numbers would you like to enter? 6
Please enter number 1 : 452
Please enter number 2 : 985
Please enter number 3 : 64
Please enter number 4 : -1693
Please enter number 5 : 9
Please enter number 6 : 836
List = [452, 985, 64, -1693, 9, 836]
The sum is 653
The min is -1693
The avg is 108.83

'''
