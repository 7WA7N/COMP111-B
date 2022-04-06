# Muhammad Ali Awan 
# 231522965
# COMP111 - B 
# Lab 4 

import math 
import random 

#! Question 1 
class sphere():

    def __init__(self,radius):
        self.radius = radius
        
    def getRadius(self):
        return print(self.radius) 

    def surfaceArea(self):
        self.surfaceArea = 4*math.pi*(self.radius**2) 
        return print(f'The surface area is, {self.surfaceArea}')

    def volume(self):
        self.volume = (4/3)*math.pi*(self.radius**3)
        return print(f'The volume is, {self.volume}')

sphere_obj = sphere(4)
sphere_obj.getRadius()
sphere_obj.surfaceArea()
sphere_obj.volume()


#! Question 2 
import random 

class PlayingCard():

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        return print(self.rank)

    def getSuit(self):
        return self.suit

    def BJValue(self): 
        if self.rank == 1:
            return print(1)  

        if self.rank >=2 and self.rank <=10:
            return print(self.rank)

        if self.rank > 10:
            return print(10) 
    
    def __str__(self):
        cardLast = ''
        if self.suit == 's':
            cardLast = 'Spades'
        if self.suit == 'd':
            cardLast = 'Diamonds'
        if self.suit == 'h':
            cardLast = 'Hearts'
        if self.suit == 'c':
            cardLast = 'Clubs'
        
        cardFirst = ''

        if self.rank >= 2 and self.rank <= 10:
            cardFirst = str(self.rank) 

        if self.rank == 1: 
            cardFirst = 'Ace'
        if self.rank == 11:
            cardFirst = 'Jack'
        if self.rank == 12:
            cardFirst = 'Queen'
        if self.rank == 13:
            cardFirst = 'King'

        return (f'{cardFirst} of {cardLast}')


# Random Generation 
n = int(input("Enter number of Cards to Generate:"))
suit = ['d','c','h','s']
for i in range(n):
    randomCard = PlayingCard(random.randint(1,13),random.choice(suit))
    print(randomCard)

    
aceofSpades = PlayingCard(1,'s')
jackofClubs = PlayingCard(11,'c')
fiveofHearts = PlayingCard(5,'h')

aceofSpades.getRank()
aceofSpades.getSuit()
aceofSpades.BJValue()
print(aceofSpades)

jackofClubs.getRank()
jackofClubs.getSuit()
jackofClubs.BJValue()
print(jackofClubs)

fiveofHearts.getRank()
fiveofHearts.getSuit()
fiveofHearts.BJValue()
print(fiveofHearts)

#! Question 3 
class Customer():
    def __init__(self,CustomerID,CurrentBalance,AccountID):
        self.CustomerID = CustomerID
        self.CurrentBalance = CurrentBalance
        self.AccountID = AccountID

    def DisplayInfo(self):
        return print(f'CustomerID:{self.CustomerID}\nCurrentBalance:{self.CurrentBalance}\nAccountID:{self.AccountID}')

customer_obj = Customer(23,23000,32423423423420)
customer_obj.DisplayInfo()

