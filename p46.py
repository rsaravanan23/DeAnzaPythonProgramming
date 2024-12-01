# p46.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a Python program to do the following:

Let the user enter a file name (such as "myMovies.txt").
Let the user enter the titles of 4 of their favorite movies using a loop.
Write using a loop the 4 movie titles to a file, one per line, and closes the file.
Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in a list, and then shows the list.
Write the titles in reverse order into a file "reverseOrder.txt"
'''


fileName = input("Enter a file name: ")
newFile = open(fileName, 'w')
for i in range(0,4,1):        
    movie  = input("Enter a movie title %s : " %(i+1))
    newFile.write(movie + '\n')

newFile.close()

newFile = open(fileName, 'r')
movieNamesAsList = newFile.read().splitlines()
newFile.close()
print(movieNamesAsList)
print()


myFile = open('reverseOrder.txt', 'w')
for i in range (3,-1,-1):
    print(movieNamesAsList[i])
    myFile.write(movieNamesAsList[i] + '\n')

myFile.close()

