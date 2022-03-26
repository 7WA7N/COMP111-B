
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

def sumEven():
    print(sum(range(2,102,2)))

sumEven()

