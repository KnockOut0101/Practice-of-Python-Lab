class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self,time_object):
        if((self.minutes + time_object.minutes) >= 60):
            self.hours = self.hours + 1 + time_object.hours
            self.minutes = self.minutes + time_object.minutes - 60
            return Time(self.hours,self.minutes)
        else:
            return Time(self.hours + time_object.hours , self.minutes + time_object.minutes)

    def Display(self):
        self.minutes = self.minutes + self.hours*60
        return print("Total Minutes:-%d"%(self.minutes))
    

    def __str__(self):
        return "The Current Time is :- {0} hours,{1} minutes".format(self.hours,self.minutes)


time1 = Time(11,10)
time2 = Time(12,50)
time3 = time1+time2
print(time3)

time3.Display()
