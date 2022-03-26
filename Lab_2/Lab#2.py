# 231522965
# Muhammad Ali Awan
# COMP-111-B

# Lab 2 


#! Question 1 

def wc(filename):

    fileData = open(filename, 'r', encoding="utf8").read()

    print('Lines:',len(fileData.splitlines()))
    print('Words:',len(fileData.split(fileData)))
    print('Characters:',len(fileData))

wc('sample.txt')

    


    
