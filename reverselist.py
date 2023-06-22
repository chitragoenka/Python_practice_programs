# write a program in Python to reverse the numbers in a list

def reverseList(list):
    for index in range((int)(len(list)/2)):
        temp=list[index]
        list[index]=list[len(list)-1-index]
        list[len(list)-1-index]=temp

    return list

list=[13,45,67,90,89,78]
list=reverseList(list)
print(list)    