# Muhammad Ali Awan 
# 231-522965
# Lab 10
# COMP111-3

from abc import ABC, abstractmethod

class Package(ABC):

    def __init__(self,
    SenderName,
    SenderAddress,
    SenderCity,
    SenderState,
    SenderZIP,
    RecepientName,
    RecepientAddress,
    RecepientCity,
    RecepientZIP,
    Weight,
    Cost):
        
        self.SenderName = SenderName
        self.SenderAddress = SenderAddress
        self.SenderCity = SenderCity
        self.SenderState = SenderState
        self.SenderZIP = SenderZIP

        self.RecepientName = RecepientName
        self.RecepientAddress = RecepientAddress
        self.RecepientCity = RecepientCity
        self.RecepientState = RecepientState
        self.RecepientZIP = RecepientZIP

        self.Weight = Weight
        self.Cost = Cost 


        if cost > 0:
            self.Cost = Cost 
        else:
            print('Error: Cost needs to be a positive value.')
        if weight > 0 :
            self.Weight = Weight
        else:
            print('Error: Weight needs to be a positive value.')

    @abstractmethod
    def calculateCost(self):
        return print(f'Total Cost:{self.Cost*self.Weight}') 

class TwoDayPackage(Package):

    def __init__(self,
    SenderName,
    SenderAddress,
    SenderCity,
    SenderState,
    SenderZIP,
    RecepientName,
    RecepientAddress,
    RecepientCity,
    RecepientZIP,
    Weight,
    Cost,FlatFee):

    self.FlatFee = FlatFee

    super().__init__(SenderName,
    SenderAddress,
    SenderCity,
    SenderState,
    SenderZIP,
    RecepientName,
    RecepientAddress,
    RecepientCity,
    RecepientZIP,
    Weight,
    Cost)
    
    def calculateCost(self):
        return print(f'Total Cost:{(self.Cost*self.Weight)+self.FlatFee}')

class OvernightPackage(Package):
    
    def __init__(self,
    SenderName,
    SenderAddress,
    SenderCity,
    SenderState,
    SenderZIP,
    RecepientName,
    RecepientAddress,
    RecepientCity,
    RecepientZIP,
    Weight,
    Cost):

    self.AdditionalFee = 200

    super().__init__(SenderName,
    SenderAddress,
    SenderCity,
    SenderState,
    SenderZIP,
    RecepientName,
    RecepientAddress,
    RecepientCity,
    RecepientZIP,
    Weight,
    Cost)
    
    def calculateCost(self):
        return print(f'Total Cost: {(self.Weight * (self.Cost+self.AdditionalFee))}')

# Driver Code
def main():
    DHL = Package('Ali','House-666, J-Town','Lahore','Punjab',54000,'Ahmed','House-333','A-Town','Karachi','Sindh',70211,60,120)
    FedEx = TwoDayPackage('Hafeez','Rahber-421, X-Town','Lahore','Punjab',54000,'Khalid','G-3233','L-Town','Karachi','Sindh',70211,190,200,500)
    UPS = OvernightPackage('Muzamil','House-700, Q-Town','Lahore','Punjab',54000,'Dudda','House-000','P-Town','Karachi','Sindh',70211,200,400)
    
    data = [DHL,FedEx,UPS]
    for objects in data:
        objects.calculateCost()
main()
        
        
