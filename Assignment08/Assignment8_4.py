
import threading
import os

def Small(data):
    list1=[]
    for i in data:
        if i>="a" and i<="z":
            list1.append(i)
    
    print("Thread Name is : {} and ID is {} ".format(threading.current_thread().name,os.getpid()))
    print("Small Letters are  : ",list1)
    print("Count of Small Letters are : ",len(list1))
                
def Capital(data):
    list2 =[]
    for i in range(len(data)):
        if data[i].isupper() == True:
            list2.append(data[i])
            
    print("Thread Name is : {} and ID is {} ".format(threading.current_thread().name,os.getpid()))
    print("Capital Letters are : ",list2)
    print("Count of capital Letters are : ",len(list2))

def Digit(data):
    list3=[]
    for i in data:
        if i.isdigit() == True:
            list3.append(i)
    
    print("Thread Name is : {} and ID is {} ".format(threading.current_thread().name,os.getpid()))
    print("Digits are",list3)
    print("Count of digits are : ",len(list3))
            

def main():
    String = input("Enetr the String which Include Capital and samll letters and digits :  ")
    
    small = threading.Thread(target=Small, args=(String,))
    
    capital = threading.Thread(target=Capital,args=(String,))
    
    digit = threading.Thread(target=Digit,args=(String,))
    
    small.start()
    capital.start()
    digit.start()
    
    small.join()
    capital.join()
    digit.join()

if __name__=="__main__":
    main()