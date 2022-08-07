
length = int(input("Enter lenght of fibonacci"))
L1=[]

def fibonacci(l1,length):
    if(len(l1) == length):
        #print(l1,"1")
        return print(l1)
    if(len(l1) == 0):
        l1.append(1)
        l1.append(2)
        #print(l1,"2")
        fibonacci(l1,length)
    else:
        next=l1[len(l1)-1]+l1[len(l1)-2]
        l1.append(next)
        #print(l1,"3")
        fibonacci(l1,length)

result = fibonacci(L1, length)

result
