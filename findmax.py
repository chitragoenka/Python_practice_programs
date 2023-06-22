# Write a Python program to find the largest number in the list

a= [10,45,67,100,14,25,60,200]

max=a[0]

for data in range(2,len(a)):
    if(max<a[data]):
        max=a[data]

print(max)

