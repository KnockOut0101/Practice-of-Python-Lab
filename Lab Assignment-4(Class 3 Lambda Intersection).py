L1 = []
L2 = []

length = int(input("Enter a length of list"))

for i in range(length):
    element1 = int(input("Enter an element for L1:-"))
    element2 = int(input("Enter an element for L2:-"))
    L1.append(element1)
    L2.append(element2)

print(L1,L2)

def intersection(l1,l2):
    return list(filter(lambda x : x in l1,l2))


result = intersection(L1,L2)

print(result)