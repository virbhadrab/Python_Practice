import threading

def Even(x):
    esum=0
    for i in range(0,len(x)):
        if x[i]%2==0:
            esum+=x[i]
    
    print("Additon of even Elements is {} ".format(esum))

def Odd(x):
    osum=0
    for i in range(0,len(x)):
        if x[i]%2!=0:
            osum+=x[i]
    
    print("Additon of even Elements is {} ".format(osum))

def main():
    X = list()
    n = int(input("Enetr the List Limit : "))
    print("Enetr the Elements in List : ")
    
    for i in range(n):
        X.append(int(input()))
        
    evenList = threading.Thread(target=Even, args=(X,))
    
    oddList = threading.Thread(target=Odd,args=(X,))
    
    evenList.start()
    oddList.start()
    
    evenList.join()
    oddList.join()

if __name__=="__main__":
    main()