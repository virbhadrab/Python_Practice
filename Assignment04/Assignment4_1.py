#1.Write a program which contains one lambda function which accepts one parameter 
# and return
#power of two.
#Input : 4 Output : 16
#Input : 6 Output : 64 


Power = lambda no : no**2

def main():
    
    num = int(input("Enter the Number : "))
    
    iret = Power(num)
    print("Poewr of {} is : ".format(num),iret)

if __name__=="__main__":
    main()