

x = (5,10,12,15)

print(x)

y = list(reversed(x))

print(y)

z = [1,2,"String",(1,2,3),"hi"]



count = 0
i=0 
while(True):
    if( isinstance(z[i],tuple) == True):
        break
    else:
        count = count + 1
        print(z[i],count)
        i= i + 1
        