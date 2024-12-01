# p8.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Multiplication Table
    Write a program to print a multiplication table for float values  0.1, 0.2 and 0.3.

    The Output should use the placeholder (%) to control column widths.

    Save and submit as p8.py

Sample output:
           	0.1	0.2	0.3
      0.1	0.01	0.02	0.03
      0.2	0.02	0.04	0.06
      0.3	0.03	0.06	0.09
'''

print("     0.1   0.2   0.3")
print("0.1  %.2f  %.2f  %.2f" %(0.1*0.1, 0.1*0.2, 0.1*0.3))
print("0.2  %.2f  %.2f  %.2f" %(0.2*0.1, 0.2*0.2, 0.2*0.3))
print("0.3  %.2f  %.2f  %.2f" %(0.3*0.1, 0.3*0.2, 0.3*0.3))

'''

===================== RESTART: C:/Users/rishi/python/p8.py =====================
     0.1   0.2   0.3
0.1  0.01  0.02  0.03
0.2  0.02  0.04  0.06
0.3  0.03  0.06  0.09

'''
