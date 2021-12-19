"""Write a program which accept one number from user and return its factorial. 
Input : 5 Output : 120""" 

def Factorial(no):
    fact = 1
    
    for i in range(1,no+1):
        fact = fact * i
    
    return fact

def main():
    ino = int(input("Enter the Number : "))
    iret = Factorial(ino)

    print("Factorial of given Nimber is : ",iret)
    
if __name__=="__main__":
    main()
        