from typing import List


list = []

for i in range(10):
    number = int(input("Enter a Number:-"))
    list.append(number)

print(list)

def Product(List):
    product = 1
    for i in range(10):
        product = product*List[i]
    print("%d"%(product))

def Largest(List):
    largest = 0
    for i in range(10):
        if (List[i]>largest):
            largest = list[i]
        else:
            continue
    print("%d"%(largest))

def Odd_count(List):
    index = 0
    while(index<10):
        count = 0
        number = List[index]
        for i in range(10):
            if (number == List[i]):
                count = count + 1
        if(count%2!=0):
            print("Counted %d this many times %d\n"%(number,count))
        else:
            print("Count not odd for number %d"%(count))
        index = index + 1

Largest(list)
Odd_count(list)
Product(list)
