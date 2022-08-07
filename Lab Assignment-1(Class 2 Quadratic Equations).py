import cmath
import math
import cmath

a = int(input("Enter value of 'a':-"))
b = int(input("Enter value of 'b':-"))
c = int(input("Enter value of 'c':-"))

d = math.sqrt(b**2 - (4*a*c))



if(d < 0):
    root1 = complex(b,d)
    root2 = complex(b,-d)
    root1 = (root1)/(2*a)
    root2 = (root2)/(2*a)

else:
    root1 = (-b - d)/(2*a)
    root2 = (-b + d)/(2*a)

print("Roots:-\n",root1,"\n",root2)