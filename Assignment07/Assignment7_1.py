def DisplayPatter(no):
    
    if(no>0):
        print("* ",end="")
        no-=1
        DisplayPatter(no)

def main():
    ino = int(input("Enter the number : "))
    DisplayPatter(ino)
    
if __name__=="__main__":
    main()