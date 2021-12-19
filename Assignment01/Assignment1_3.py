#Write a program which contains one function named as Add() which accepts two numbers 
#from user and return addition of that two numbers. 
#Input : 11 5 Output : 16

def Add(value1,value2):
    
    iret = value1 + value2
    
    return iret
    
def main():
    
    no1 = int(input("Enter the First Number :"))
    no2 = int(input("Enter the Second Number :"))
    
    ians = Add(no1,no2)
    
    print("Addition of given 2 Number's is :",ians)

if __name__=="__main__":
    main()