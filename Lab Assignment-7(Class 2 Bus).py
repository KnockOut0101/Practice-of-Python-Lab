class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        self.fare_rate = self.capacity * 100
        self.actual_fare = (10/100)*self.fare_rate + self.fare_rate
        return self.actual_fare

Bus1 = Bus("School Volvo", 12, 50)

print("Total Bus Fare:-", Bus1.fare())