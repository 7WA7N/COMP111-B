# Muhammad Ali Awan
# 231-522965
# Lab 3 

# Question 1 
def BinomialCoefficient(n,k):
    if k == 1:
        return n 
    elif n < k:
        return 0 
    else:
        return BinomialCoefficient(n-1,k-1) + BinomialCoefficient(n-1,k)

print(BinomialCoefficient(10,6))

# Question 2
def max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = max(list[1:])
        return m if m > list[0] else list[0]

list = [33,44,66,22,10]
print(max(list))

# Question 3 
def rec(x,y):
    if y > 0:
        return x * rec(x,y-1)
    return 1

rec(3,2)