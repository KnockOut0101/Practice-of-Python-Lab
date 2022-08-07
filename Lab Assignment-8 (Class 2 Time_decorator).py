import time


def measure_time(function):
    def time_cal(msg):
        time1 = time.time()
        function(msg)
        time2 = time.time()
        print("Reached here")
        print(time2-time1)
    return time_cal

def name(msg):
    print(msg)
    return time.sleep(4)

measure_time(name)

@measure_time
def name(msg):
    print(msg)
    return time.sleep(4)

name("kshitij")