"""
4.Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
Element to search : 5 
Output : 3      """

def Frequency(no1,element):
    cont = 0
    value = element
    for i in range(len(no1)):
        if (value == no1[i]):
            cont+=1
    
    return cont

def main():
    list1 = []
    limit = int(input("Enter the limit : "))
    
    print("Enter the Elements : ")
    for i in range(limit):
        list1.append(int(input()))
    
    svalue = int(input("Enter the search value : "))
    
    ians = Frequency(list1,svalue)
    print("Frequency Of Given Search Element is : ",ians)
    
if __name__=="__main__":
    main()