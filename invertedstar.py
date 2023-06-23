# write a program to print the inverted stars

def generateStar(num):
    for i in range(num):
        print(i*' '+ (num-i) *'*')

generateStar(10)
