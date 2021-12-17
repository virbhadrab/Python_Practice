import random

X = int(input("Enetr the number :"))

list = ["Your Number is :","Aapne dile kiya gaya Number hai :"]

item = random.choice(list)

if X >=0 :
    print(item,X)
else:
    print("Fuck Off")