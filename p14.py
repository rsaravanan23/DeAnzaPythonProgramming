# p14.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that asks the user for day and month of a birthday.

The program then tells the Zodiac signs that will be compatible with that birthday

Constellation	English Name		    Dates	
-Aries		The Ram			Mar. 21–Apr. 19	
-Taurus		The Bull		Apr. 20–May 20	
-Gemini		The Twins		May 21–June 21	
-Cancer		The Crab		June 22–July 22	
-Leo		The Lion		July 23–Aug. 22	
-Virgo		The Virgin		Aug. 23–Sept. 22	
-Libra		The Balance	        Sept. 23–Oct. 23	
-Scorpio	The Scorpion	        Oct. 24–Nov. 21	
-Sagittarius	The Archer		Nov. 22–Dec. 21	
-Capricorn	The Goat		Dec. 22–Jan. 19	
-Aquarius	The Water Bearer        Jan. 20–Feb. 18	
-Pisces		The Fishes	        Feb. 19–Mar. 20	
'''

month = int(input("Please enter your month of birth: "))
day = int(input("Please enter your day of birth: "))

if ( month == 3 and day >= 21 ) or ( month == 4 and day <= 19 ):
    print("You are a Aries")

if ( month == 4 and day >= 20 ) or ( month == 5 and day <= 20 ):
    print("You are a Taurus")

if ( month == 5 and day >= 21 ) or ( month == 6 and day <= 21 ):
    print("You are a Gemini")

if ( month == 6 and day >= 22 ) or ( month == 7 and day <= 22 ):
    print("You are a Cancer")

if ( month == 7 and day >= 23 ) or ( month == 8 and day <= 22 ):
    print("You are a Leo")

if ( month == 8 and day >= 23 ) or ( month == 9 and day <= 22 ):
    print("You are a Virgo")

if ( month == 9 and day >= 23 ) or ( month == 10 and day <= 23 ):
    print("You are a Libra")

if ( month == 10 and day >= 24 ) or ( month == 11 and day <= 21 ):
    print("You are a Scorpio")

if ( month == 11 and day >= 22 ) or ( month == 12 and day <= 21 ):
    print("You are a Sagittarius")

if ( month == 12 and day >= 22 ) or ( month == 1 and day <= 19 ):
    print("You are a Capricorn")

if ( month == 1 and day >= 20 ) or ( month == 2 and day <= 18 ):
    print("You are a Aquarius")

if ( month == 2 and day >= 19 ) or ( month == 3 and day <= 20 ):
    print("You are a Pisces")


'''

===================== RESTART: C:/Users/rishi/python/p14.py ====================
Please enter your month of birth: 2
Please enter your day of birth: 21
You are a Pisces

'''
