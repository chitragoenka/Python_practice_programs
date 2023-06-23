# write a program that takes a list of numbers and outputs two lists of odd and even numbers separately

def oddeven(list):
    oddNumbers=[]
    evenNumbers=[]
    for data in list:
        if(data%2==0):
            evenNumbers.append(data)
        else:
            oddNumbers.append(data)
    return oddNumbers,evenNumbers

x=[12,13,9,10,32,33]
odd,even=oddeven(x)
print(odd)
print(even)            