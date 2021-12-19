"""Write a program which accept one number form user and return addition of its factors. 
Input : 12 Output : 16 (1+2+3+4+6) """

def FactAdd(no):
    
    temp = int(no/2)
    sum = 0
    
    for i in range(1,temp+1):
        if (no%i == 0):
            sum = sum + i
    
    return sum

def main():
    ino = int(input("Enter the number : "))
    iret = FactAdd(ino)
    
    print("Addition of given Numbers Factor's is : ",iret)
    
if __name__=="__main__":
    main()