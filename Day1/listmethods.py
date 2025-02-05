# names=["joy","meul","brin","kauf"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# print(names[1:])
# print(names[2:3])

# print(names[:])
# print(names[:4]) #to print entire list

#insert method
# lst=[12,34,5,6,79]
# lst.insert(1,14) #insert (index,value)
# print(lst)

# if 5 in lst:
#     print(lst.index(5)) # to get index of specific element

# del lst[0]
# print(lst)


# print(lst.pop()) # By default removes the last element
# print(lst)


# print(lst.pop(1)) #removing the element from index 1
# print(lst)


# lst.remove(lst[0]) #removes specific element first occurence
# print(lst)

# lst.clear()
# print(lst)

# #2-d dimensional list 
# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in mat:
#     for j in i:
#         print(j)




employees=[
    {"name":"Alice","salary":50000},
    {"name":"Bob","salary":60000},
    {"name":"Charlie","salary":40000},
    {"name":"jax","salary":50000},
    {"name":"white","salary":60000},
    {"name":"fring","salary":40000}
]
print(sorted(employees,key=lambda x:x["name"]))
print(sorted(employees,key=lambda x:x["salary"]))
# print(sorted(employees)

sorted_employees=sorted(employees,key=lambda x:(x["salary"],x["name"]))
semp=sorted(employees,key=lambda x:(-x["salary"],x["name"]))
print(sorted_employees)
print(semp)

# from functools import reduce

# numbers=[1,2,3,4]
# numb=reduce(lambda x,y:x*y,numbers)