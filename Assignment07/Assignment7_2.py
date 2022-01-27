def DisplayNumber(no):
    
    if(no>0):
        DisplayNumber(no-1)
        print(no," ",end="")
        

def main():
    ino = int(input("Enter the Number : "))
    DisplayNumber(ino)

if __name__=="__main__":
    main()