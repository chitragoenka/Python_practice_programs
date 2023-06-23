# write a program to calculate median of numbers in a list

def median(input):
    input.sort()
    print(input) # This is to check if the list is sorted in ascending order

    if(len(input)%2==1):
        return (input[(int)(len(input)/2)])
    else:
        return (input[(int)(len(input)/2)]+input[(int)(len(input)/2)-1])/2
    
x=[10,15,4,18,30,100,50,40]
output=median(x)
print(output)    