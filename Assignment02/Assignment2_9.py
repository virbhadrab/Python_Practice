""" Write a program which accept number from user and return number of digits in that number. 
Input : 5187934 Output : 7  """

def Display(no):
    
    count = 0

    while(no > 0):
        temp = no%10
        count+=1
        print(count)
        no = int(no/10)
   
   
def main():
    
    ino = int(input("Enter the no. of rows : "))
    
    Display(ino)

if __name__=="__main__":
    main()