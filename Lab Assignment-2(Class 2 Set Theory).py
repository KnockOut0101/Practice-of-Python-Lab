

Mathematics = {"Rajesh", "Jay", "Abhishek", "Urmila", "Kadambini", "Naina", "Amar", "Angad", "Avesh"}
Economics = {"Urmila", "Amar", "Sujata", "Nahira", "Avnish", "Surendra", "Kadambini"}
Physics = {"Chitra", "Bala", "Ramesh", "Nagendra", "Avnish", "Urmila", "Naina", "Abhijeet", "Avesh"}

All_Three = Mathematics.intersection(Economics.intersection(Physics))

Economics_only = Economics.difference(Mathematics.union(Physics))

Math_Eco_not_Physics = Mathematics.union(Economics) - Physics

Subjects_two = Mathematics.intersection(Economics).union(Economics.intersection(Physics).union(Physics.intersection(Mathematics))) - All_Three

Subjects_two_least = Subjects_two.union(All_Three)

Only_one = Mathematics.union(Economics.union(Physics)) - Subjects_two_least
print("ALL Three :-\n",All_Three)
print("Economics Only :-\n",Economics_only)
print("Math & Eco but not Physics :-\n",Math_Eco_not_Physics)
print("Only 2 Sunjects:-\n", Subjects_two)
print("Least 2 Sunjects:-\n", Subjects_two_least)
print("Only one Subject:-\n",Only_one)