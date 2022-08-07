

L1 = [] 

no_elements = int(input("Enter no. of elements"))
for i in range(no_elements):
    number = int(input("Enter no. in form of elements:-"))
    L1.append(number)

def Check_unique(list):
    L2 = []
    for i in range(len(list)):
        count = 0
        for j in range(len(list)):
            if(list[i] == list[j] and i!=j):
                count= count + 1
        if (count == 0):
            L2.append(list[i])
    return L2

unique = Check_unique(L1)

print(unique)

            

        


