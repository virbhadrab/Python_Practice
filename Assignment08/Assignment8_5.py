
import multiprocessing
import threading


def Display():
    for i in range(1,51):
        print(i,end=" ")

    print()
    
def DisplayX():
    print()
    i=50
    while (i>=1):
        print(i,end=" ")
        i-=1

def main():
    
    thread1 = threading.Thread(target=Display)
    thread2 = threading.Thread(target=DisplayX)
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()
    
if __name__=="__main__":
    main()