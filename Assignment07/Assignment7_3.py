def DisplayNumber(no):
    
    if(no>0):
        print(no," ",end="")
        DisplayNumber(no-1)

def main():
    ino = int(input("Enter the Number : "))
    DisplayNumber(ino)

if __name__=="__main__":
    main()