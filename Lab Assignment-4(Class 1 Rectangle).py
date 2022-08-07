TLCx = int(input("Enter Top Left Corner X-Co-ordinate:-"))
TLCy = int(input("Enter Top Left Corner Y-Co-ordinate:-"))
BRCx = int(input("Enter Bottom Right Corner X-Co-ordinate:-"))
BRCy = int(input("Enter Bottom Right Corner Y-Co-ordinate:-"))

if (TLCx < BRCx and TLCy > BRCy ):
    Breadth = TLCx-BRCx
    Length = TLCy-BRCy
    Area = Length*Breadth

    print("Area-: %d Breath-:%d Length-:%d"%(Area,Breadth,Length))
else:
    print("Invalid Input")
