import threading
from tkinter.messagebox import NO


def evenFactorSum(No):
    efact=0
    for i in range(1,No):
        if No%i==0 and i%2==0:
            efact+=i
    
    print("Addition of even factors is : ",efact)

def oddFactorSum(No):
    ofact=0
    for i in range(1,No):
        if No%i==0 and i%2!=0:
           ofact+=i
    
    print("Additon of Odd Factors are  : ",ofact) 

def main():
    
    no = int(input("Enetr the Number : "))
    
    evenFactor = threading.Thread(target=evenFactorSum, args=(no,))  
    oddFactor = threading.Thread(target=oddFactorSum, args=(no,))
    
    evenFactor.start()
    oddFactor.start()
    
    evenFactor.join()
    oddFactor.join()
    
    print("Exit from : ",threading.current_thread().name)

if __name__=="__main__":
    main()