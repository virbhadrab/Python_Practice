# #5.Write a program which contains filter(), map() and reduce() in it. Python application which 
# #contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# #should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
# #return Maximum number from that numbers. (You can also use normal functions instead of 
# #lambda functions). 
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62

from functools import reduce


Prime = lambda no :all(no%i!=0 for i in range(2,int(no/2)+1)) if no>1 else None

Product = lambda no : no*2

Maximum =(lambda no1,no2 : no1 if(no1>no2) else no2)

def main():
    data = list()
    size  = int(input("Enter the size of list : "))
    
    print("Enter the element in list : ")
    for i in range(size):
        data.append(int(input()))

    print("Entered List is : ",data)
    
    PrimeData = list(filter(Prime,data))
    print("After Filter List is : ",PrimeData)

    mapData = list(map(Product,PrimeData))
    print("After mapped List is : ",mapData)
    
    reducedata = reduce(Maximum,mapData)
    print("Reduced Output is : ",reducedata)
    
if __name__=="__main__":
    main()