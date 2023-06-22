# write a program in python to remove the characters in the odd place 

str="abcdefghijk"

# first way commented

'''str=str[1::2]
print(str)'''

# second way of doing the same

output=''
for index in range(len(str)):
    if(index%2!=0):
        output+=str[index]

print(output)        