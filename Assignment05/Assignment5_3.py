class Arithmetic:
    
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    
    def Accept(self):
        self.value1 = int(input("Enter the first number : "))
        self.value2 = int(input("Enter the second number : "))
    
    def Addition(self):
        ans = self.value1 + self.value2
        return ans
    
    def Substraction(self):
        ans = self.value1 - self.value2
        return ans
    
    def Multuplication(self):
        ans = self.value1 * self.value2
        return ans
    
    def Division(self):
        if (self.value2 != 0):
            ans = self.value1 / self.value2
            return ans
        else:
            return None
            
    
def main():
    obj1 = Arithmetic()
    
    obj1.Accept() 
    ret = obj1.Addition()
    print("Addition is : ",ret)
    
    obj1.Accept()
    ret1 = obj1.Substraction()
    print("Substraction is : ",ret1)
    
    obj1.Accept()
    ret2 = obj1.Multuplication()
    print("Multiplication is  : ",ret2)
    
    obj1.Accept()
    ret3 = obj1.Division()
    if (ret3 != None):
        print("Division is : ", ret3)
    else:
        print("Division is not Possible Please Enter valid value :")

if __name__=="__main__":
    main()