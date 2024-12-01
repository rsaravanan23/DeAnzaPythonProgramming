# p18.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Write a program that displays the characters in the ASCII character table from
! to ~.

Display ten characters per line.

The characters are separated by exactly one space.

! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
Every Key on your keyboard has a numerical representation. This number is
called ASCII value.

The ASCII values are shown in the ASCII table below.
'''

count = 0

# ascii value of ! = 33
# ascii value of ~ = 126
for ascii in range (33,127,1):
    print(chr(ascii), " ", end = "")
    count = count + 1
    if count == 10:
        print()
        count = 0

'''

===================== RESTART: C:/Users/rishi/python/p18.py ====================
!  "  #  $  %  &  '  (  )  *  
+  ,  -  .  /  0  1  2  3  4  
5  6  7  8  9  :  ;  <  =  >  
?  @  A  B  C  D  E  F  G  H  
I  J  K  L  M  N  O  P  Q  R  
S  T  U  V  W  X  Y  Z  [  \  
]  ^  _  `  a  b  c  d  e  f  
g  h  i  j  k  l  m  n  o  p  
q  r  s  t  u  v  w  x  y  z  
{  |  }  ~  

'''
