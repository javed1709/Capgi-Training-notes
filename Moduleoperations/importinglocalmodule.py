# import moduleoperations as cal
from moduleoperations import * # import all
from moduleoperations import add,sub # importing specific functions

def compute(x):
    a=int(input("Enter the value"))
    b=int(input("Enter the value"))
    match x:
        case "add":
            print(f"a+b={add(a,b)}")
        case "sub":
            print(f"a-b={sub(a,b)}")

x=input("Enter the coice:")
compute(x)