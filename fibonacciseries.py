# Write a python program to print first n numbers of Fibonacci series

def generateFibonacciNumbers(number):
    firstNumber=0
    secondNumber=1
    if(number<1):
        return
    
    for i in range(number):
        print(secondNumber)
        thirdNumber=firstNumber+secondNumber
        firstNumber=secondNumber
        secondNumber=thirdNumber

generateFibonacciNumbers(10)