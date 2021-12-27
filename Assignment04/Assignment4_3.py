#3.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that
#numbers. 

from functools import reduce

CheckRange = lambda no : (no>=70 and no<=90)

AddData = lambda no : no +10

Product = lambda no1,no2 : no1*no2

def main():
    data = []
    
    size = int(input("Enter the list size : "))
    
    print("Enter the data into list : ")
    for i in range(size):
        data.append(int(input()))
    
    print("Your Entered List Element's are ",data)
    
    
    filterList = list(filter(CheckRange,data))
    print("List After Filter : ",filterList)
    
    mapList  = list(map(AddData,filterList))
    print("List After map : ",mapList)
    
    product = reduce(Product,mapList)
    print("Output Of Product : ",product)

if __name__=="__main__":
    main()