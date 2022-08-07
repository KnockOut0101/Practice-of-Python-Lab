

A = int(input("Enter 1st no. :-"))
B = int(input("Enter 2nd no. :-"))

def calculation(a,b):
    c= a+b
    d= a-b
    return c,d

add,sub = calculation(A,B)

print("Sum:- %d AND Substraction:- %d"%(add,sub))

