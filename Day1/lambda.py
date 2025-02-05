# def multi(n):
#     return lambda x: x*n

# tw=multi(2)
# print(tw(3))

#lambda with multiple parameters
# def lmb():
#     n1=int(input("Enter the value:"))
#     n2=int(input("Enter the value:"))
#     x=lambda v1,v2:v1*v2
#     return f"product of {n1} & {n2}={x(n1,n2)}"

# print(lmb())
# x=lambda y:"even" if y%2==0 else "odd"
# n=int(input("Enter the number:"))
# print(x(n))

#assignment: calculate the total amount based on price and quantity
# def amnt():
#     price=int(input("Enter the price:"))
#     quantity=int(input("Enter the quantity:"))
#     x=lambda v1,v2:v1*v2
#     return f"Amount is:{x(price,quantity)}"
# print(amnt())

#lambda with map, map() is function which takes the a function and collection(i.e.list,tuple..) and apply computation in function on each value of list/tuple 

# def lambdawithmap():
#     l=[2,3,4,5,6]
#     res=map(lambda x:x*3,l)
#     print(list(res))

# lambdawithmap()

# def lambdawithfilter():
#     l=[2,3,4,5,6]
#     res=filter(lambda x:x>3,l)
#     print(list(res))

# lambdawithfilter()

def singlelineinput():
    l=list(map(int,input("Enter the list").split()))
    print(l)

singlelineinput()