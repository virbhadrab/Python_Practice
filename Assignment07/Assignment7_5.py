fact =1
def Factorial(no):
    global fact
    
    if no>0:
        fact = fact*no
        Factorial(no-1)
    
    return fact

def SmartFactorial(Fun_Fact):
    def Inner(no):
        if no<0:
            no=-no
        return Fun_Fact(no)

    return Inner

Factorial = SmartFactorial(Factorial)

def main():
    no = int(input("Enter the number : "))
    iret = Factorial(no)
    
    print("Factorial of {} is {} ".format(no,iret))

if __name__=="__main__":
    main()