SeatNo = int(input("Enter Seat no.:-"))
Tags = ["LB","MB","UB","LB","MB","UB","SL","SU"]

if(SeatNo%8 == 0 and SeatNo<=80):
    print(Tags[0])
if(SeatNo%8 == 1 and SeatNo<=80):
    print(Tags[1])
if(SeatNo%8 == 2 and SeatNo<=80):
    print(Tags[2])
if(SeatNo%8 == 3 and SeatNo<=80):
    print(Tags[3])
if(SeatNo%8 == 4 and SeatNo<=80):
    print(Tags[4])
if(SeatNo%8 == 5 and SeatNo<=80):
    print(Tags[5])
if(SeatNo%8 == 6 and SeatNo<=80):
    print(Tags[6])
if(SeatNo%8 == 7 and SeatNo<=80):
    print(Tags[7])

else:
    print("Invalid Input")
