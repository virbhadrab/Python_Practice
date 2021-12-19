#Write a program which accept name from user and display length of its name. 
#Input : Marvellous Output : 10

def DisplayLen(name1):
    
    ino = len(name1)
    return ino

def main():
    
    name = input("Enetr Your name :")
    iret =DisplayLen(name)
    
    print("length of given name is :",iret)

if __name__=="__main__":
    main()