class Triangle:
    def __init__ (self, side):
        self.side = side 

    def area(self):
        return(self.side/2)

    def perimeter(self):
        return((1+2+self.side))

t = float(int(input("Enter the value of Triangle: ")))

t1 = Triangle(t)

print("Area of Triangle: ", t1.area())
print("Perimeter of Triangle: ", t1.perimeter())