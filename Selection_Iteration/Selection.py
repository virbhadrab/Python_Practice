
def Maximun(value1,value2):
    if (value1 > value2):
        return value1
    else:
        return value2

def main():
    
    no1 = int(input("Enetr the first no :"))
    
    no2 = int(input("Enetr the seconf no :"))
    
    ret = Maximun(no1,no2)
    
    print("Maximun number is  : ", ret)
    
if __name__=="__main__":
    main()