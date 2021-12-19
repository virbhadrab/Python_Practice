"""     Write a program which accept one number and display below pattern. 
Input : 5 
Output : 1 2 3 4 5 
         1 2 3 4 5
         1 2 3 4 5
         1 2 3 4 5 
         1 2 3 4 5          """


def Display(row,col):
    
    for i in range(1,row+1):
        for j in range(1,col+1):
            print(j," ",end="")
        print()

def main():
    irow = int(input("Enter the number of row's : "))
    
    icol = int(input("Enter the number of Column's : "))
    
    Display(irow,icol)

if __name__=="__main__":
    main()