class rectangle:
    def __init__(self,l,b,x=0,y=0):
        self.length = l
        self.breadth = b
        self.coordinatex = x
        self.coordinatey = y
        

    def area(self):
        area = self.length*self.breadth
        return print(area)

    def permeter(self):
        perimeter = 2*(self.length+self.breadth)

    def Intersecting_area(self,shape):
        A = (self.length + self.coordinatex)-shape.coordinatex
        B = (self.breadth + self.coordinatey)-shape.coordinatey
        if(A>0 and B>0):
            print("Intersection exists")
            print("Area :- %d"%(A*B))



        

rectangle1 = rectangle(10,20)
rectangle2 = rectangle(10,20,5,5)
rectangle1.Intersecting_area(rectangle2)