"""Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
parameters as number and perform the operation. Write on python program which call all the 
functions from Arithmetic module by accepting the parameters from user."""

from Arithmetic import *

def main():
    
    value1 = int(input("Enter the first Number :"))
    value2 = int(input("Enetr the Second number :"))
    
    Add(value1,value2)
    Sub(value1,value2)
    Mult(value1,value2)
    Div(value1,value2)

if __name__=="__main__":
    main()