class Circle:
    def __init__(self):
        self.radius=float(input("enter a radius: "))
        self.pi=3.14
        self.cir_area=0
        self.cir_peri=0
        self.area()
        self.perimeter()

    def area(self):
        self.cir_area=self.pi*self.radius**2
        print (self.cir_area)

    def perimeter(self):
        self.cir_peri=2*self.pi*self.radius
        print (self.cir_peri)
