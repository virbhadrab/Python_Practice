class Circle:
    
    PI = 3.14
    
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circum=0.0

    def Accept(self):
        self.radius = float(input("Enter the radius : "))
        
    def CalculateArea(self):
        self.area = Circle.PI * self.radius*self.radius
        
    def CalculateCircum(self):
        self.circum = 2*Circle.PI*self.radius
        
    def Display(self):
        print()
        print("Radius of circle is  :",self.radius)
        print("Area of Circle is : ",self.area)
        print("Circumferance of circle is : ",self.circum)
    
    
def main():
    
    obj1 = Circle()
    
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircum()
    obj1.Display()

if __name__=="__main__":
    main()
    
