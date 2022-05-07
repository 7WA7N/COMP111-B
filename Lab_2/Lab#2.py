# Muhammad Ali Awan 
# 231522965
# COMP111 - B 
# Lab 2


#! Question 1 

def wc(filename):

    fileData = open(filename, 'r', encoding="utf8").read()

    print('Lines:',len(fileData.splitlines()))
    print('Words:',len(fileData.split(fileData)))
    print('Characters:',len(fileData))

wc('sample.txt')

    
#! Question 2 

def square1(x):
    return x*x

def square2(x):
    print(x*x)

a = square1(4)
b = square2(4)


#! Question 3 

def summation(n): 
    total, k = 0, 1 
    while k <= n: 
        total, k = total + k*k*k, k + 1 
    return total 
result = summation (3)

#! Question 4

x = 5
def square(x):
 return x*x
def double(x):
 return square(x+1) - square(x) - 1
double(x)


    
