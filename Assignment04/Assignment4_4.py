# 4.Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# should filter out all such numbers which are even. Map function will calculate its square. 
# Reduce will return addition of all that numbers. 
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204

from functools import reduce

Even = lambda no : (no%2 ==0)

MapSquare = lambda no : no*no

Addition = lambda no1,no2 : no1+no2

def main():
    
    data = list()
    size = int(input("Enter the Size of list : "))
    
    print("Enter the elements into list : ")
    
    for i in range(size):
        data.append(int(input()))
    
    print("Your Enterd list is : ",data)
    
    evenData = list(filter(Even,data))
    print("After Filter Even elements into list : ",evenData)
    
    squareData = list(map(MapSquare,evenData))
    print("List After Map : ",squareData)
    
    reduceData = reduce(Addition,squareData)
    print("Reduce Output is : ",reduceData)

if __name__=="__main__":
    main()