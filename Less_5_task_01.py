
#Less_5_task_01
#The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers


#Varian_001

import random

list = [random.randint(1,1000000000), random.randint(1,1000000000),random.randint(1,1000000000),random.randint(1,1000000000),
        random.randint(1,1000000000), random.randint(1,1000000000),random.randint(1,1000000000),random.randint(1,1000000000),
        random.randint(1,1000000000),random.randint(1,1000000000)]
print (list)
print('Max element in list', max(list))



#Varian_002

list = [random.randint(1000000000, 10000000000) for x in range(0, 10)]
print(list)
print('Max element in list', max(list))


# не понимаю, как здесь использовать цикл while
