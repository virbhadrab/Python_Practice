"""Write a program which accept one number and display below pattern. 
Input : 5 
Output : * * * * * 
         * * * * *
         * * * * * 
         * * * * * 
         * * * * *  """
         
def Display(row,col):
    for i in range(row):
        for j in range(col):
            print("* ",end="")
        print()

def main():
    
    irow = int(input("Enter the no. of rows :"))
    icol = int(input("Enter the no. of coumns"))
    
    Display(irow,icol)
    
if __name__=="__main__":
    main()
    