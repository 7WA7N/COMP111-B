# Muhammad Ali Awan
# 231522965
# COMP111 - B
# Assignment 1 

import random

# Question 1 
def num_to_name(num):
    names = {
        0: "zero ",
        1: "one ",
        2: "two ",
        3: "three ",
        4: "four ",
        5: "five ",
        6: "six ",
        7: "seven ",
        8: "eight ",
        9: "nine ",
    }

    if num == 0:
        return ''
    
    return num_to_name(num // 10) + names[num % 10]


# Question 2 
class Dice():
    def __init__(self):
        self.face = random.randint(1,6)
    
    def roll(self):
        self.face = random.randint(1,6)

    def showFace(self):
        return self.face

class Statistics():
    def __init__(self):
        self.data1 = []

    def data_entry(self,data):
        self.data1.append(data)

    def sum_data(self):
        sum = 0 
        for values in self.data1:
            sum += values
        return sum

    def mean_data(self):
        sum = 0 
        for values in self.data1:
            sum += values
        return (sum/len(self.data1))
    
    def stddev_data(self):
        mean = self.mean_data()
        data2 = []

        for values in self.data1:
            data2.append((values-mean)**2)
        
        sum2 = 0 
        for values in data2:
            sum2 += values
        
        mean2 = sum2/len(data2)

        return (mean2**(1/2))

    def getMax(self):
        max = 0 
        for values in self.data1:
            if values > max:
                max = values

        return (max)

    def getMin(self):
        min = 7
        for values in self.data1:
            if values < min:
                min = values
        return (min)


def main():

    # Question 1 
    print(num_to_name(12345))

    # Question 2
    face = input('Enter a number between 1 and 6: ')
    num_experiments = int(input('Enter the number of experiments: '))

    statistics = Statistics()
    dice = Dice()

    for i in range(num_experiments):
        for i in range(50):
            dice.roll()
        statistics.data_entry(dice.showFace())

    print('\n The Statistics are:')
    print(f'Sum of Items: {statistics.sum_data()}')
    print(f'Mean of Items: {statistics.mean_data()}')
    print(f'Standard Deviation of Items: {statistics.stddev_data()}')
    print(f'Max of Items: {statistics.getMax()}')
    print(f'Min of Items: {statistics.getMin()}')

    with open('data.txt','w') as f:
        f.write('Problem 1:\n\n')
        f.write(num_to_name(12345))
        f.write('\n\nProblem 2:\n\n')
        f.write(f'Sum of Items: {statistics.sum_data()}\n')
        f.write(f'Mean of Items: {statistics.mean_data()}\n')
        f.write(f'Standard Deviation of Items: {statistics.stddev_data()}\n')
        f.write(f'Max of Items: {statistics.getMax()}\n')
        f.write(f'Min of Items: {statistics.getMin()}\n')


main()