Side1 = int(input("Enter 1st side of triangle:-"))
Side2 = int(input("Enter 2nd side of triangle:-"))
Side3 = int(input("Enter 3rd side of triangle:-"))

##Sides = [Side1,Side2,Side3]
##Index = [0,1,2]
##Status = False

if(Side1 == Side2 or Side1 == Side3 or Side2 == Side3):
    print("Isosceles")
if(Side1 == Side2 == Side3):
    print("Equilateral")
if((Side1*Side1)+(Side2*Side2)==(Side3*Side3) or (Side2*Side2)+(Side3*Side3)==(Side1*Side1) or (Side1*Side1)+(Side3*Side3)==(Side2*Side2)):
    print("Right-Angle")
