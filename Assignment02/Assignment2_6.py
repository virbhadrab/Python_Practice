"""  Write a program which accept one number and display below pattern. 
Input : 5 
Output : 
        * * * * * 
        * * * * 
        * * * 
        * * 
        *  """
        
def Display(row,col):
    
    for i in range(1,row+1):
        for j in range(1,col+1):
            if (i<=j):
                print("*  ",end="")
        print()

def main():
    
    irow = int(input("Enter the no. of rows : "))
    
    icol = int(input("Enter the number of column's : "))
    
    Display(irow,icol)

if __name__=="__main__":
    main()