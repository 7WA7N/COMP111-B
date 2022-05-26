# Muhammad Ali Awan 
# 231522965 
# COMP-111 - B
# Lab 7 


# Task 1 
class Address():
    def __init__(self,HNo,StNo,Town,City):
        self.HNo = HNo
        self.StNo = StNo
        self.Town = Town 
        self.City = City
    
    def display(self):
        print("House No. :",self.HNo)
        print("Student No.:",self.StNo)
        print("Town:",self.Town)
        print("City:",self.City)

class Student():
    def __init__(self,id,name,HNo,StNo,Town,City):
        self.id = id
        self.name = name
        self.address = Address(HNo,StNo,Town,City)

class Faculty():
    def __init__(self,id,name,HNo,StNo,Town,City):
        self.id = id
        self.name = name
        self.address = Address(HNo,StNo,Town,City)

class Staff():
    def __init__(self,id,name,HNo,StNo,Town,City):
        self.id = id
        self.name = name
        self.address = Address(HNo,StNo,Town,City)


# Task 2 
class Bank():
    def __init__(self):
        self.name = 'Al Baraka'
        self.accountsList = []

class Account():
    def __init__(self,title,accountNo,accountType,Balance):
        self.title = title
        self.accountNo = accountNo
        self.accountType = accountType
        self.Balance = Balance
        self.accountsList.append(Account(title,accountNo,accountType,Balance))
    
    def withdraw(self, amount):
        if amount <= balance:
            self.balance = self.balance - amount 
            print('Cash Withdrawn: PKR',amount)
            print('Remaining Balance: PKR',self.balance)
        elif amount > balance:
            print("Insufficient Funds for Transfer")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Amount Depositied: PKR',amount)
        print('Total Balance: PKR',self.balance)


# Driver Code
def main():
    
    # Task 1
    student1 = Student(2345,'Ali Awan','House #15','Street #1','Johar Town','Lahore')
    faculty1 = Faculty(4545,'Minahil Baig','House #456','Street #2','RedBull Society','Lahore')
    staff1 = Staff(6969,'Taha Nadeem','House #20','Street #9','Qarshi Town','Lahore')

    student1.address.display()
    faculty1.address.display()
    staff1.address.display()

    # Task 2 
    AlBaraka = Bank()
    Account1 = Account('Ali Awan',234567,'Savings',156000)
    Account1.withdraw(20000)
    Account1.deposit(50000)

    def findAccount(search):
        for i in range(len(Bank.accountsList)):
            if Bank.accountsList[i].title == search:
                print(Bank.accountsList[i].title, 'is found in the list.')
            else: 
                print('Bank Account was not found')
    findAccount('Ali Awan')




main() 
