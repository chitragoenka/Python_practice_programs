#Write a program to find the sum of digits in any number

def calculateSum(number):
    sum=0
    while(number>0):
        modulo=number%10
        sum+=modulo
        number=int(number/10)
    return sum    

number=1896
print(calculateSum(number))        
