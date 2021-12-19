""" Write a program which accept number from user and return addition of digits in that number. 
Input : 5187934 Output : 37 """

def DigitAdditon(no1):
    
    sum = 0
    while(no1>0):
        temp = no1%10
        sum = sum + temp
        no1 = int(no1/10)
    
    return sum
    
def main():
    value = int(input("Enter the number :"))
    
    iret = DigitAdditon(value)
    
    print("Addition Of All Digit's are :",iret)

if __name__=="__main__":
    main()