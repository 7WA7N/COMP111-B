# Muhammad Ali Awan 
# 231522965
# COMP111 - B 
# Lab 1


#! Question 1 
rate = int(input("Enter Rate"))
initialAmount = 1 
year = 0 
total = 0


while total <= initialAmount*2:
    interest = (rate * initialAmount * 1)/100
    total = total + interest
    year += 1
    continue
print('Year is', year)

#! Question 2 
from math import sqrt

def isPrime(n):
    prime_check = 0

    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_check = 1
                break
        if (prime_check == 0):
            print(n,"is a Prime Number")
        else:
            print(n,"isn't a Prime Number")

isPrime(5)
isPrime(2)
isPrime(4)

#! Question 3 
mystery = {'Ali': 22, 'Saleha': 19, 'Ahsan': 21}
def ageing(dict):
    for i in mystery.keys():
        mystery[i] += 1
    return print(mystery)

ageing(mystery)

#! Question 4 
student_id = input("Enter your Student ID:")
courses = open('Classes.txt','r')
print("Student ID:",student_id)
for course in courses:
    course = course.rstrip()

    lines=open(course+".txt",'r')
    for line in lines:
        parts = line.split()
        if student_id == parts[0]:
            print(course,parts[1])
    lines.close()

courses.close()