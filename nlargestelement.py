#write a program to print nth largest number in the list

def largestN(list,number):
    list.sort()
    list=list[::-1]
    return list[number-1]

x=[45,67,12,100,13]
print(largestN(x,2)) #to print the 2nd largest number in the list x
print(largestN(x,3)) #print the 3rd largest no.