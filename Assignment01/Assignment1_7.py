#Write a program which contains one function that accept one number from user and returns 
#true if number is divisible by 5 otherwise return false. 
#Input : 8 Output : False 
#Input : 25 Output : True 

def Divisible(value1):
    if (value1%5 == 0):
        return True
    else:
        return False

def main():
    
    ino = int(input("Enetr the Number :"))
    
    bret = Divisible(ino)
    
    print(bret)

if __name__=="__main__":
    main()