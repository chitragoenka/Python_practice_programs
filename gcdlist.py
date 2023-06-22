#write a program in Python to print the GCD of all the numbers in the list

import math

def gcdList(list):
    gcd=math.gcd(list[0],list[1])

    for index in range(2,len(list)):
        gcd=math.gcd(gcd,list[index])

    return gcd

list=[12,18,30,96,84,72] 
print(gcdList(list))   