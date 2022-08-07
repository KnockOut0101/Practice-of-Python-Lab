
import datetime


x = datetime.datetime(2000,1,1)
y = datetime.datetime(1993,10,28)


class person():
    def __init__(Self,DOB,Current = datetime.datetime.now()):
        Self.DOB = DOB
        Self.Current_date = Current
    
    @property
    def Age(Self):
        Self.age = Self.Current_date - Self.DOB
        return Self.age

    @Age.setter
    def Age(Self,a):
        Self.DOB = a
        return Self.age

    @Age.deleter
    def Age(Self):
        Self.DOB = None
        Self.Current_date = None

Kshitij = person(x)
print(Kshitij.Age)
Kshitij.Age = y
print(Kshitij.Age)
delattr(Kshitij,'Age')
#delattr(Kshitij,'Current_date')
print(Kshitij.Age)