# write a program to remove duplicate numbers in a list

def removeDuplicate(input):
    setObject=set(input)
    return list(setObject)

x=[1,2,3,4,4,5,6,4,7,4,6,2,8]
x=removeDuplicate(x)
print(x)