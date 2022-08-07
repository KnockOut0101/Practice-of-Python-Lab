
List= []

for i in range(5):
    Roll_no = int(input("Enter Role No.:-"))
    Name = input("Enter a Name:-")
    age = int(input("Enter Age:-"))
    branch = input("Enter Branch:-")
    dict = {"RollNo": Roll_no, "Name":Name, "Age": age , "Branch": branch}
    List.append(dict)


roll_no = int(input("Enter no. to check:-"))
for i in range(5):
    if(roll_no == List[i]["RollNo"]):
        print("found")
        print(List[i])
    elif(roll_no != List[i]["RollNo"] and i == len(List)):
        print("Not found")

