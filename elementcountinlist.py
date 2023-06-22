#write a program to count the number of occurences of an element in a list

def calOccurence(list,item):
    count=0
    for data in list:
        if(data == item):
            count+=1
    return count

x=[1,4,2,3,5,3,6,3,7,2,3]
print(calOccurence(x,3))      

#Another way of doing the same
#print(x.count(3))