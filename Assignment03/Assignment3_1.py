"""
1.Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. 
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56 
Output : 130    """

def ListAddition(no1):
    sum=0
    
    for i in range(len(no1)):
        sum = sum + int(no1[i])
        print(sum)
    
    return sum

def main():
    list1 = []
    limit = int(input("Enetr the Number of Element's : "))
    
    print("Enter the Number's : ")
    
    for i in range(limit):
        list1.append(int(input()))
    
    print(list1)
    lans = ListAddition(list1)
    
    print("Addition Of All Element's : ",lans)

if __name__=="__main__":
    main()