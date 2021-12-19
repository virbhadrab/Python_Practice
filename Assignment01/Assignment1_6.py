#Write a program which accept number from user and check whether that number is positive or 
#negative or zero. 
#Input : 11 Output : Positive Number 
#Input : -8 Output : Negative Number 
#Input : 0 Output : Zero

def ChkNum(value1):
    
    if (value1 > 0):
        print("Positive Number :")
    elif (value1 < 0):
        print("Negative Number :")
    else:
        print("Zero")
        
def main():
    
    ino = int(input("Enter the Number :"))
    
    ChkNum(ino)

if __name__=="__main__":
    main()