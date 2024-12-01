# p39.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that asks the user to enter a sentence.
Your program will:

Show how many words are in the sentence 
Show the last word of the sentence
Ask the user to enter their own word, and count how many times their word appears in the sentence
Note: you can't use the built-in python function count() to do this!
'''

sentence = input("Please enter a sentence: ")
print()
sentenceSplit = sentence.split(" ")
last = sentenceSplit[len(sentenceSplit)-1]


print("There are", len(sentenceSplit), "words in the sentence you entered")
print("The last element of the list is", last)

word = input("Please enter a word to search: ")
count = 0
for i in range(0,len(sentenceSplit),1):
    if sentenceSplit[i] == word: 
        count += 1

print("The word '" + word + "' appears " + str(count) + " times in the sentence.") 


'''

======================= RESTART: C:\Users\rishi\python\p39.py =======================
Please enter a sentence: i like to play violin and i like basketball

There are 9 words in the sentence you entered
The last element of the list is basketball
Please enter a word to search: like
The word 'like' appears 2 times in the sentence.

'''
