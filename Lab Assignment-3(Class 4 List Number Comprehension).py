number1 = [[j for j in range(1000) if j%i==0 and i not in ] for i in range(2,9)]
number_range = range(26)
number2 = [i for i in number_range if i*i>50]
print(number2,"\n\n\n\n")
print(number1)