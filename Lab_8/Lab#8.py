# Muhammad Ali Awan 
# 231-522965
# COMP111-B 
# Lab 8 

# Question 1 
class Polygon():
    def __init__(self,numOfSides):
        self.numOfSides = numOfSides
    def inputSides(self, sides):
        self.numOfSides = sides
    
class Triangle(Polygon):
    def __init__(self,numOfSides,base,height):
        self.base = base 
        self.height = height
        super().__init__(numOfSides)
        self.area = self.getArea()
    
    def getArea(self):
        return (1/2)*(self.base+self.height)
    def displayArea(self):
        print(self.area)
        
class Square(Polygon):
    def __init__(self,numOfSides,allSides):
        self.allSides = allSides
        super().__init__(numOfSides)
        self.area = self.getArea()
        
    def getArea(self):
        return (self.allSides**2)
    
    def displayArea(self):
        print(self.area)
        
# Question 2 
class Person():
    def __init__(self, PersonID, PersonName):
        self.PersonID = PersonID
        self.PersonName = PersonName

class Patient(Person):
    def __init__(self, PersonID,PersonName,PatientDisease):
        self.PatientDisease = PatientDisease
        self.Treatment = None 
        super().__init__(PersonID,PersonName)
        
    def Chart(self):
        print('Patient ID:',self.PersonID)
        print('Patient Name:',self.PersonName)
        print('Disease:',self.PatientDisease)
        print('Treatment:',self.Treatment)
        
class Doctor(Person):
    def __init__(self, PersonID,PersonName):
        super().__init__(PersonID,PersonName)
    
    def treat(self, patient, Treatment):
        patient.Treatment = Treatment 
        print('Treatment:', patient.Treatment)
        

def main():
    triangle = Triangle(3,12,6)
    triangle.displayArea()
    
    square = Square(4,10)
    square.displayArea()
    
    patient = Patient(1111, 'Ali Awan', 'Swine Flu')
    doctor = Doctor(2222, 'Ahmed Khan')
    doctor.treat(patient, 'Medication')
    patient.Chart()

main()
        
        