dict1 = {"Sedan": 1500, "SUV": 2000,"Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600,"Bicycle": 7, "Motorcycle": 110}
list_weight = [x for x in dict1 if dict1[x]<5000]
print(list_weight)