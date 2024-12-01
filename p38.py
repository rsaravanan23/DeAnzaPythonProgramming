# p38.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that asks the user to enter a sentence.

The program then finds the longest word in the sentence, and shows it.

Note: The use of python functions max() and sorted() is not permitted!
'''

sentence = input("Please enter a sentence:  ")
sentenceSplit = sentence.split(" ")


longest = sentenceSplit[0] 
for i in range(1,len(sentenceSplit),1):
    if len(sentenceSplit[i]) > len(longest): 
           longest = sentenceSplit[i] 

print('The longest word is', longest)
print(longest, 'has', len(longest), 'characters')

'''

==== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p34.py ====
Please enter a sentence:  what are you doing tomorrow hello
The longest word is tomorrow
tomorrow has 8 characters

'''
