"""Write a program which accept one number for user and check whether number is prime or not. 
Input : 5 Output : It is Prime Number"""

def Prime(no):
    
    temp = int(no/2)
    bert = True
    for i in range(1,temp+1):
        if(no%i == 0):
            bret = False
        else:
            bret = True
    
    return bret
    
def main():
    
    ino = int(input("Enter the Number : "))
    
    bans = Prime(ino)
    
    if (bans==True):
        print("Number is prime ")
    else:
        print("Number is not prime ")

if __name__=="__main__":
    main()