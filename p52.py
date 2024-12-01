# p52.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
Create a class Item which has
- instance variables: itemName, itemCost
- class variable: numberItems (gets increased every time a new Item is created)
- a default constructor that allows the user to set itemName and itemCost
( the default constructor sets itemName="apple" itemCost=2.49 if the user does not specify them)
- function to show() the item name and cost
- function to get() and set() the item name and cost

Create a list named groceryBag to store the objects:
- Fill the list with several Item's such as eggs, milk, carrots, bread, apples, each with different price.
- use Item.numberItems to show how many items you have created.
- use a loop to calculate and show the totalCost for all the items in the bag
'''


class Item:
    numberItems = 0

    def __init__(self, itemName="apple", itemCost= 2.49):

        Item.numberItems += 1

        self.name = itemName
        self.cost = itemCost

    def show(self):
        print("The item name is", self.name,"and item cost is", self.cost)
        #print("The item cost is", self.cost)

    def getName(self):
        return self.name
    
    def getCost(self):
        return self.cost
    
    def setName(self):
        self.name = itemName

    def setCost(self):
        self.cost = itemCost

        

groceryBag = []
eggs = Item('eggs',3.76)
groceryBag.append(eggs)

apple = Item('apple',2.49)
groceryBag.append(apple)

milk = Item('milk',5.23)
groceryBag.append(milk)

carrot = Item('carrot',1.94)
groceryBag.append(carrot)

bread = Item('bread',1.34)
groceryBag.append(bread)

print("Grocery Bag:")

for i in range (0,5,1):
    groceryBag[i].show()

    

totalCost = 0
for i in range(0,len(groceryBag),1):
    totalCost += groceryBag[i].getCost()
print("\nTotal cost:", totalCost)



print("\nThere are", Item.numberItems, "items.")


'''

====================== RESTART: C:\Users\rishi\python\p52.py ======================
Grocery Bag:
The item name is eggs and item cost is 3.76
The item name is apple and item cost is 2.49
The item name is milk and item cost is 5.23
The item name is carrot and item cost is 1.94
The item name is bread and item cost is 1.34

Total cost: 14.76

There are 5 items.

'''

