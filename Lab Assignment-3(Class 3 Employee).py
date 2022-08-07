

name = input("Enter name of employee:-")
salary = input('Salary of said Employee (default is 9000):-')

def Employee(Name, Salary=9000):
    return(print("Name:-%s Salary:-%d"%(Name,Salary)))

Employee(name)
Employee(name,int(salary))