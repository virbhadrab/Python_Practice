"""
2.Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 
Input : Number of elements : 7 
Input Elements : 13 5 45 7 4 56 34 
Output : 56     """

def Maximum(no1):
    max = 0
    
    for i in range(len(no1)):
        if (max>=no1[i]):
            max = max
        else:
            max = no1[i]

    return max

def main():
    limit = int(input("Enter the limit : "))
    
    list1 = []

    print("Enter the element's : ")
    for i in range(limit):
        list1.append(int(input()))
    
    ians = Maximum(list1)    
    print("Maximum Number in List is : ",ians)
    
if __name__=="__main__":
    main()