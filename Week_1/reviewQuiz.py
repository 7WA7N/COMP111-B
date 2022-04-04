# 231522965
# Muhammad Ali Awan
# COMP-111-B
# Lab 1 

#! Question 1 
# Write a short Python function,
# isMultiple(n,m), which takes two integer values 
# and returns True if n is a multiple of m, 
# so n = m*i for some integer i and 
# False otherwise. 


def isMultiple(n,m):
    if n % m == 0:
        return print(True)
    else: 
        return print(False)
isMultiple(8,2) 

#! Question 2 
# The sum of all even numbers 
# between 2 and 100 (inclusive).

def sumAllEven():
    sum = 0
    for x in range(2,102,2):
        sum += x 
    return sum
sumAllEven()

#! Question 3 
# Write down the sum of all squares between
# 1 and 100, inclusive. Using a function. 

def sumOfsquares():
    total = 0 
    for x in range(1,101):
        square = x*x
        total = total + square
    return print(total)
sumOfsquares()

#! Question 4 
# The sum of all Odd Numbers, between
# a and b, inclusive. 

def sumOfOdds(a,b):
    total = 0 
    for x in range(a,b+1):
        if x % 2 != 0:
            total += x
    return total

sumOfOdds(1,100)



