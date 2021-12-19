def Addition(value1,value2):
    ans = 0
    ans = value1 + value2
    
    return ans

def main():
    no1 = 0
    no2 = 0
    ret = 0
    
    print("Enetr first no :")
    no1 = int(input())
    
    print("Enetr Second no :")
    no2 = int(input())
    
    ret = Addition(no1,no2)
    
    print("Additon of 2 no :",ret)
    
if __name__=="__main__":
    main()