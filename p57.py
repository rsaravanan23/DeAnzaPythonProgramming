# p57.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
In a weighted alphabet, every symbol is assigned a positive real number called a weight.

A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

1) The mass of each possible amino acid is given in the file aa.txt

- Put the contents of the above file into a dictionary:  dictionary [ 'Letter' ] = value

2) Ask the user to enter an amino acid string consisting of only the letters shown in file aa.txt
- if the user enters an incorrect letter, then the program asks for another string

3) Calculate the total weight of the amino acid
 a) use characters of the string as keys for the dictionary from (1)
 b) sum the weights for all letters and show the total weight
'''

myFile = open('aa.txt', 'r')
aLine = myFile.read().splitlines()

aDictionary = {}



for i in range(0,len(aLine),1):
    everyLine = aLine[i].split()             #    ['A','71.03711']
    aDictionary[everyLine[0]] = everyLine[1]
    
myFile.close()


invalidValues = ['B', 'J', 'O', 'U', 'X', 'Z']

while True:
    wasInvalidValueGiven= False
    sum = 0
    valid = input('Please enter the letters you would like to weight: ')    #fdisdi
    valid = valid.upper()
    inputValues = list(valid)
    # ['f','d','i','s','d','i']
    #check if input has any invalid values
    for i in range (0,len(inputValues),1):
        if inputValues[i] in invalidValues:
            wasInvalidValueGiven = True
            break                              #if there are invalid values then break for loop and restart while loop
        else:
            sum += float(aDictionary[inputValues[i]])
    if wasInvalidValueGiven == True:
        continue
    else:
        break

print("Sum:", sum)


'''
========================= RESTART: C:\Users\rishi\python\p57.py ========================
Please enter the letters you would like to weight: bdgjuyo
Please enter the letters you would like to weight: acghp
Sum: 465.17943

'''
                
            
