# p17.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Suppose that the tuition for a university is $10,000 this year and increases
5% every year.

Write a program that computes the tuition in ten years and displays a table of
the years and tuition costs. A loop must be used.
'''

tuition = 10000
for year in range (1,11,1):
    print("Year: %3i" %year, "    Tuition:", tuition)
    tuition = tuition*1.05

'''

===================== RESTART: C:/Users/rishi/python/p17.py ====================
Year:   1     Tuition: 10000
Year:   2     Tuition: 10500.0
Year:   3     Tuition: 11025.0
Year:   4     Tuition: 11576.25
Year:   5     Tuition: 12155.0625
Year:   6     Tuition: 12762.815625000001
Year:   7     Tuition: 13400.956406250001
Year:   8     Tuition: 14071.004226562502
Year:   9     Tuition: 14774.554437890627
Year:  10     Tuition: 15513.28215978516


'''
