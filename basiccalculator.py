# write a program to perform arithmetic calculations

def calculator():
    flag=True
    while(flag):
        print("Select Option:")
        print("1 : Addition")
        print("2 : Subtraction")
        print("3 : Multiplication")
        print("4 : Division")
        option=(int)(input("Please enter your choice: "))
        firstNumber=(int)(input("Please enter first number: "))
        secondNumber=(int)(input("Please enter second number: "))
        if(option==1):
            print("Sum of {} and {} = {}".format(firstNumber,secondNumber,firstNumber+secondNumber))
        elif (option==2):
            print("Difference of {} and {} = {}".format(firstNumber,secondNumber,firstNumber-secondNumber))
        elif (option==3):
            print("Product of {} and {} = {}".format(firstNumber,secondNumber,firstNumber*secondNumber))       
        elif (option==4):
            print("Division of {} and {} = {}".format(firstNumber,secondNumber,firstNumber/secondNumber))

        cont=input("Do you want to continue? Press 'Y' if you want to continue: ")
        if (cont.upper()!='Y'):
            flag=False       

calculator()  



