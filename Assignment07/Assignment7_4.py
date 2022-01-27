sum =0
def Summation(no):
    global sum
    
    if no!=0:
        rem = no%10
        sum = sum+rem
        no = no//10
        Summation(no)
        
    return sum

def SmartSummation(func_no):
    
    def Inner(no):
        if(no<0):
            no=-no
        
        return func_no(no)

    return Inner

Summation = SmartSummation(Summation)

def main():
    ino = int(input("Enter the Number : "))
    iret = Summation(ino)
    print("Summation of {} is : ".format(ino),iret)

if __name__=="__main__":
    main()