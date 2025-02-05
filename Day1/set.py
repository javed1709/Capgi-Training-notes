# x=set()

# x={"Javed",12,19.3,"r"}
# print(x)

# #adding o=element using add method
# x.add(11)
# print(x)

# #adding elements using the set() constructor
# lst=[1,2,3,4,1]
# y=set((lst))
# print(y)

# print()
# lst=[1,2,3,4,1]
# # x.update(y)
# x.update(lst)
# x|=y #update shortcut
# print(x)
# x.discard(19.3)
# print(x)

x={1,2,3}
y={3,5,2}
print(x.union(y))
print(x.difference(y)) #- shortcut
x.difference_update(y) # removes all common elements of x,y in x and store in x
# x.intersection_update(y) #put's common elements of x,y store in x and store in x
print(x)
print(x.intersection(y)) 

#copying set
tmp=x.copy()
print(tmp)
tmp.add(2)
print(tmp)
tmp.remove(2)
print(tmp)

st={"clean","sweep","algo",1,-1}
for i in st:
    print(i)

#taking run time input to set
# a=set()
# n=int(input("Enter the elements:"))
# for i in range(0,n):
#     x=int(input("Enter the value:"))
#     a.add(x)

# for i in a:
#     print(i)

#subset
st1={1,2,3}
st2={2,3}
print(st2.issubset(st1))

print(st1.issuperset(st2))