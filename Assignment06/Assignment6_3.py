class Numbers:
    
    def __init__(self,value):
        
        self.no = value
    
    def ChkPrime(self):
        flag=True
        
        if (self.no==1):
            flag=False
        else:
            for i in range(2,int(self.no/2)):
                if (self.no%i==0):
                    flag=False
                    break
                else:
                    flag=True
        
        if (flag==True):
            return True
        else:
            return False
        
    def Factors(self):
        fact1 = []
        for i in range(1,self.no):
            if (self.no%i==0):
                fact1.append(i)
        
        return fact1     
    
    def SumFactors(self): 
        sum =0       
        for i in range(1,self.no):
            if (self.no%i==0):
              sum = sum + i  

        return sum
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.no):
            if (self.no%i == 0):
                sum = sum + i

        if (sum==self.no):
            return True
        else:
            return False    
        
    
def main():
    value = int(input("Enter the Number : "))
    obj = Numbers(value)

    print(end="\n")
    bret = obj.ChkPrime()
    if bret == True:
        print("Number is Prime : ")
    else:
        print("Number is not Prime : ")
        
    bret1 = obj.ChkPerfect()
    if bret1 == True:
        print("Number is perfect : ")
    else:
        print("Number is not Perfect no. ")
        
    iret = obj.Factors()
    print("Factors are : ",end=" ")
    
    for i in range(len(iret)):
        print(iret[i],end=" ")
        
    iret1 = obj.SumFactors()
    print("\nSum of Factors are : ",iret1)
    
if __name__=="__main__":
    main()