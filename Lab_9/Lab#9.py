# Muhammad Ali Awan 
# 231522965
# COMP111-B 
# Lab 9 


# Question 1 
class Payment():
    def __init__(self,payment):
        self.payment = payment 
    def paymentDetails(self):
        print(f'The total payment is {self.payment}')


class CashPayment(Payment):
    def __init__(self,payment):
        super().__init__(payment)
    def paymentDetails(self):
        print(f'The total payment in cash is {self.payment}')


class CardPayment(Payment):
    def __init__(self,payment):
        super().__init__(payment)
    def paymentDetails(self):
        print(f'The total payment from your card is {self.payment}')


class CreditCard():
    def __init__(self,Name,ValidThru,CardNumber,payment):
        self.Name = Name
        self.ValidThru = ValidThru
        self.CardNumber = CardNumber
        self.CardPaymentObj = CardPayment(payment)
    def paymentDetails(self):
        print(f'Name: {self.Name}')
        print(f'Valid Thru: {self.ValidThru}')
        print(f'Card Number: {self.CardNumber}')
        print(f'Payment Details: {self.CardPaymentObj.payment}')

def main():
    
    MyCard = CreditCard('Ali Awan','09/24','2224-4235-4775-4209',20000)
    cashPayment1 = CashPayment(20000)
    cashPayment2 = CashPayment(1000000)
    cardPayment1 = CardPayment(100)
    cardPayment2 = CardPayment(200)
    

    data = [cashPayment1,cashPayment2,cardPayment1,cardPayment2,MyCard]
    for objects in data:
        objects.paymentDetails()

main()

        

