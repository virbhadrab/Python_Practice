from itertools import count
from ntpath import join
from re import X
import threading

def Even(x):
    count=x
    ecount=1
    even = list()
    i=1
    j=1
    while ecount<=count:
        if i%2==0:
            even.append(i)
            ecount+=1
        i+=1

    print("First {} Even Numbers : ".format(X))
    for i in even:
        print(i,end=" ")

def Odd(x):
    odd = list()
    ocount=1
    count=x
    j=1
    while ocount<=count:
        if j%2!=0:
            odd.append(j)
            ocount+=1
        j+=1
    
    print("\n First {} Odd numbers : ".format(X))
    for j in odd:
        print(j,end=" ")
    

def main():
    X = int(input("Enter Display Even and Odd Numbers Limit : "))
    
    even = threading.Thread(target=Even, args=(X,))
    odd  = threading.Thread(target=Odd, args=(X,))
    
    even.start()
    odd.start()
    
    even.join()
    odd.join()
    

if __name__=="__main__":
    main()