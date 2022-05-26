# Muhammad Ali Awan 
# 231-522965
# COMP111-B
# Assignment 2 


# Task 1 
class Person():
    def __init__(self, PersonName):
        self.PersonName = PersonName

class Route():
    def __init__(self,TravelTime,Distance,Source,Destination,Fare):
        self.TravelTime = TravelTime
        self.Distance = Distance
        self.Source = Source
        self.Destination = Destination
        self.Fare = Fare

class Vehicle():
    def __init__(self,Manufacturer,Cylinders,OwnerName):
        self.Manufacturer = Manufacturer
        self.Cylinders = Cylinders
        self.OwnerPersonObject = Person(OwnerName)

class Truck(Vehicle):
    def __init__(self,Manufacturer,Cylinders,OwnerName,LoadCapacity,TowingCapacity,TravelTime,Distance,Source,Destination,Fare):
        self.LoadCapacity = LoadCapacity
        self.TowingCapacity = TowingCapacity
        self.RouteObject = Route(TravelTime,Distance,Source,Destination,Fare)
        super().__init__(Manufacturer,Cylinders,OwnerName)
    def routeInfo(self):
        print("Route Information")
        print("Travel Time:",self.RouteObject.TravelTime)
        print("Distance:",self.RouteObject.Distance)
        print("Source:",self.RouteObject.Source)
        print("Destination:",self.RouteObject.Destination)
        print("Fare:",self.RouteObject.Fare)

class Bus(Vehicle):
    def __init__(self,Manufacturer,Cylinders,OwnerName,Passengers,LuggageWeight,TravelTime,Distance,Source,Destination,Fare): 
        self.Passengers = Passengers
        self.LuggageWeight = LuggageWeight
        self.RouteObject = Route(TravelTime,Distance,Source,Destination,Fare)
        super().__init__(Manufacturer,Cylinders,OwnerName)
    def routeInfo(self):
        print("Route Information")
        print("Travel Time:",self.RouteObject.TravelTime)
        print("Distance:",self.RouteObject.Distance)
        print("Source:",self.RouteObject.Source)
        print("Destination:",self.RouteObject.Destination)
        print("Fare:",self.RouteObject.Fare)


# Task 2
from abc import ABC, abstractmethod

class Player():
    def __init__(self,Name,Matches):
        self.Name = Name
        self.Matches = Matches
    def Display(self):
        print("Name:",self.Name)
        print("Matches:",self.Matches)
    
    @abstractmethod
    def PlayerType():

class Batsman(Player):
    pass

class Bowler(Player):
    pass

    
 











































# Main Function 
def main():
    
    print("Task 1")
    truck1 = Truck("Ford",4,"Ali Awan",5000,2000,25,150,'Sargodah','Khushab',2300)
    truck2 = Truck("BMW",4,"Ali Awan",2400,2000,360,2400,'Hafeezabad','Karachi',4200)
    bus1 = Bus("Mercedes",4,"Ali Awan",100,25,25,150,'Lari Adda','Multan Chungi',500)
    bus2 = Bus("Suzuki Wagon",4,"Ali Awan",100,100,21,150,'Hafeez Center','University of Toronto',6500)

    data = [truck1,truck2,bus1,bus2]
    for objects in data:
        print('---------------------------------------------------')
        print('Manufacturer:',objects.Manufacturer)
        print('Cylinders:',objects.Cylinders)
        print('Owner Name:',objects.OwnerPersonObject.PersonName)
        print('---------------------------------------------------')
        objects.routeInfo()
        print('---------------------------------------------------')
        print('\n')

    # Task 2

main()