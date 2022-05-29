# Muhammad Ali Awan
# 231-522965
# COMP111-B
# Assignment 2


# Task 1
class Person():
    def __init__(self, PersonName):
        self.PersonName = PersonName

class Route():
    def __init__(self, TravelTime, Distance, Source, Destination, Fare):
        self.TravelTime = TravelTime
        self.Distance = Distance
        self.Source = Source
        self.Destination = Destination
        self.Fare = Fare

class Vehicle():
    def __init__(self, Manufacturer, Cylinders, OwnerName):
        self.Manufacturer = Manufacturer
        self.Cylinders = Cylinders
        self.OwnerPersonObject = Person(OwnerName)

class Truck(Vehicle):
    def __init__(self, Manufacturer, Cylinders, OwnerName, LoadCapacity,
                 TowingCapacity, TravelTime, Distance, Source, Destination,
                 Fare):
        self.LoadCapacity = LoadCapacity
        self.TowingCapacity = TowingCapacity
        self.RouteObject = Route(TravelTime, Distance, Source, Destination,
                                 Fare)
        super().__init__(Manufacturer, Cylinders, OwnerName)

    def routeInfo(self):
        print("Route Information")
        print("Travel Time:", self.RouteObject.TravelTime)
        print("Distance:", self.RouteObject.Distance)
        print("Source:", self.RouteObject.Source)
        print("Destination:", self.RouteObject.Destination)
        print("Fare:", self.RouteObject.Fare)

class Bus(Vehicle):
    def __init__(self, Manufacturer, Cylinders, OwnerName, Passengers,
                 LuggageWeight, TravelTime, Distance, Source, Destination,
                 Fare):
        self.Passengers = Passengers
        self.LuggageWeight = LuggageWeight
        self.RouteObject = Route(TravelTime, Distance, Source, Destination,
                                 Fare)
        super().__init__(Manufacturer, Cylinders, OwnerName)

    def routeInfo(self):
        print("Route Information")
        print("Travel Time:", self.RouteObject.TravelTime)
        print("Distance:", self.RouteObject.Distance)
        print("Source:", self.RouteObject.Source)
        print("Destination:", self.RouteObject.Destination)
        print("Fare:", self.RouteObject.Fare)


# Task 2
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, Name, Matches):
        self.Name = Name
        self.Matches = Matches

    def Display(self):
        print("Name:", self.Name)
        print("Matches:", self.Matches)

    @abstractmethod
    def PlayerType(self, playerType):
        self.PlayerType = 'Batsman' or 'Bowler'
        return self.PlayerType

class Batsman(Player):
    def __init__(self, Name, Matches):
        super().__init__(Name, Matches)
        self.PerMatchScore = []
        i = 0
        while i < Matches:
            score = int(
                input(f"Enter the score of match {i+1} for {self.Name} :"))
            self.PerMatchScore.append(score)
            i += 1

        self.TotalScore = sum(self.PerMatchScore)

    def CalculateAverage(self):
        self.Average = self.TotalScore / len(self.PerMatchScore)
        return print(f'{self.Name}\'s average score is {self.Average}')

    def Display(self):
        print('Name:', self.Name)
        print('Matches:', self.Matches)
        print('Per Match Score:', self.PerMatchScore)
        print('Total Score:', self.TotalScore)

    def PlayerType(self):
        self.PlayerType = 'Batsman'
        return print(self.PlayerType)

class Bowler(Player):
    def __init__(self, Name, Matches):
        super().__init__(Name, Matches)
        self.PerMatchWickets = []
        i = 0
        while i < Matches:

            wickets = int(
                input(
                    f"Enter the wickets taken in match {i+1} for {self.Name} :"
                ))
            self.PerMatchWickets.append(wickets)
            i += 1

        self.NoOfWickets = sum(self.PerMatchWickets)

    def CalculateAverage(self):
        self.Average = self.NoOfWickets / len(self.PerMatchWickets)
        return print(f'{self.Name}\'s average wickets taken is {self.Average}')

    def Display(self):
        print('Name:', self.Name)
        print('Matches:', self.Matches)
        print('Per Match Wickets:', self.PerMatchWickets)
        print('No Of Wickets:', self.NoOfWickets)

    def PlayerType(self):
        self.PlayerType = 'Bowler'
        return print(self.PlayerType)


# Task 3
class CarbonFootprint(ABC):
    def __init__(self):
        self.ElectricityEmissionFactor = 1.37
        self.C02Emissions = 0
        self.PricePerKWH = 8.00
        self.PricePerThousandCubicFeetAvg = 3.00
        self.NaturalGasEmissionFactor = 120.61
        self.PoundsOfC02EmittedPerGallon = 19.4
        self.EmissionsOfOtherGreenhouseGases = 100 / 95
        self.WeeksInAYear = 52

    @abstractmethod
    def getCarbonFootprint(self):
        pass

class Building(CarbonFootprint):
    def __init__(self):
        self.color = 'The Building is White'
        CarbonFootprint.__init__(self)
        self.AvgElectricityUsage = int(
            input("Enter your Building's Average Electricity Bill: "))
        self.AvgNaturalGasUsage = int(
            input("Enter your Building's Natural Gas Usage: "))

    def getCarbonFootprint(self):
        self.Electricity = (self.AvgElectricityUsage / self.PricePerKWH
                            ) * self.ElectricityEmissionFactor * 12
        self.NaturalGas = (self.AvgElectricityUsage /
                           self.PricePerThousandCubicFeetAvg
                           ) * self.NaturalGasEmissionFactor * 12
        self.C02Emissions = self.NaturalGas + self.Electricity
        return print(f'C02 Emissions in Pounds: {self.C02Emissions}')

class Car(CarbonFootprint):
    def __init__(self):
        self.color = 'The Car is Black'
        CarbonFootprint.__init__(self)
        self.MilesDrivenPerWeek = int(input("Enter Number of Miles Driven: "))
        self.FuelEfficiency = int(input('Enter Fuel Efficiency of Car: '))
        

    def getCarbonFootprint(self):
        self.C02Emissions = ((self.MilesDrivenPerWeek * self.WeeksInAYear) / self.FuelEfficiency) * self.PoundsOfC02EmittedPerGallon * self.EmissionsOfOtherGreenhouseGases
        return print(f'C02 Emissions in Pounds: {self.C02Emissions}')

class Bicycle(CarbonFootprint):
    def __init__(self):
        self.color = 'The Bike is Blue'
        CarbonFootprint.__init__(self)

    def getCarbonFootprint(self):
        self.C02Emissions = 0
        return print(f'C02 Emissions in Pounds: {self.C02Emissions}')


# Main Function
def main():

    print("## Task 1 ##")
    truck1 = Truck("Ford", 4, "Ali Awan", 5000, 2000, 25, 150, 'Sargodah',
                   'Khushab', 2300)
    truck2 = Truck("BMW", 4, "Ahmed Awan", 2400, 2000, 360, 2400, 'Hafeezabad',
                   'Karachi', 4200)
    bus1 = Bus("Mercedes", 4, "Fazal Awan", 100, 25, 25, 150, 'Lari Adda',
               'Multan Chungi', 500)
    bus2 = Bus("Suzuki Wagon", 4, "Kashif Awan", 100, 100, 21, 150,
               'Hafeez Center', 'University of Toronto', 6500)

    data = [truck1, truck2, bus1, bus2]
    for objects in data:
        print('\n')
        print('---------------------------------------------------')
        print('Manufacturer:', objects.Manufacturer)
        print('Cylinders:', objects.Cylinders)
        print('Owner Name:', objects.OwnerPersonObject.PersonName)
        print('---------------------------------------------------')
        objects.routeInfo()
        print('---------------------------------------------------')
        print('\n')

    print('## Task 2 ##')
    print('\n')

    batsman1 = Batsman('Shahid Afridi', 3)
    bowler1 = Bowler('Gul Khan', 3)

    for objects in [batsman1, bowler1]:
        print('\n')
        objects.Display()
        objects.CalculateAverage()
        objects.PlayerType()

    print('## Task 3 ##')
    print('\n')

    building1 = Building()
    print('\n')
    bike1 = Bicycle()
    print('\n')
    car1 = Car()
    print('\n')

    data = [building1, bike1, car1]

    for objects in data:
        print(objects.color)
        objects.getCarbonFootprint()
        print('\n')


main()