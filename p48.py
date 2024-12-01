# p48.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program which reads the data from file sunspots.txt

...and computes the average for each year, writing them one per line to a file averages.txt (as shown below):

Note: You can only use code that you have learned how to write from this class website.

Do not google solutions or use any built-in python functions like: sum, sort, sorted, average, map, etc !!!
'''

aFile = open('sunspots.txt','r')
bFile = open('averages.txt','w')    


fileAsListOfLines = aFile.read().splitlines()

for j in range (0,len(fileAsListOfLines),1):
    aLineAsList = fileAsListOfLines[j].split()
    sumOfDataInEachLine = 0
    for i in range (1,len(aLineAsList),1):
        sumOfDataInEachLine += float(aLineAsList[i])
    avg = sumOfDataInEachLine/len(aLineAsList)

    bFile.write(str(avg) + '\n')
    
bFile.close()
aFile.close()


''''
averages.txt file is also submitted

'''

