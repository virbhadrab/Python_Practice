class BookStore:
    
    NoOfBooks = 0
    
    def __init__(self,bookName,authorName):
        self.Name = bookName
        self.Author= authorName

        BookStore.NoOfBooks+=1
    
    def Display(self):
        
        print("{} by {} ".format(self.Name,self.Author),end="  ")
        print("No. of Books : ",BookStore.NoOfBooks)

def main():
    
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()
    
    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__=="__main__":
    main()
        