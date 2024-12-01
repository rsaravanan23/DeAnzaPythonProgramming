# p43.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
The function returns the sorted list in ascending order if parameter 'reverse' is False.
The function returns the sorted list in descending order if parameter 'reverse' is True.
'''

numList = [5,3,7,2]

def sortedList (aList, reverse):
    
    #ascending
    for j in range (0,len(aList),1):
        for i in range (0,len(aList)-1,1):
            if aList[i] > aList[i+1]:
                temp = aList[i]   
                aList[i] = aList[i+1] 
                aList[i+1] = temp
    if reverse ==  True:
        print(aList)

    #descending
    for j in range (0,len(aList),1):
        for i in range (0,len(aList)-1,1):
            if aList[i] < aList[i+1]:
                temp = aList[i]   
                aList[i] = aList[i+1] 
                aList[i+1] = temp
    if reverse ==  False:
        print(aList)
        

sortedList (numList, True)
sortedList (numList, False)


'''

======================= RESTART: C:\Users\rishi\python\p43.py =======================
[2, 3, 5, 7]
[7, 5, 3, 2]


'''





    
