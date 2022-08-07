from typing import List


List1 = range(1,1001)

print(List1,"\n")

Listx8 = [x for x in List1 if x%8==0 ]
Listn6 = [x for x in List1 if '6' in str(x)]

print(Listx8,"\n",Listn6)