# write a program to print multiplication table

def multiplicationTable(num):
    for i in range(10):
        print( "{} * {} = {}".format(num,i+1,num*(i+1)) )

multiplicationTable(8)        