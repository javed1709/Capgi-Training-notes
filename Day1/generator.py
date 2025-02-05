# def disp(a,b):
#     yield a
#     yield b

# x,y=disp(10,20)
# print(x)
# print(y)




# def disp1(a,b):
#     yield a
#     yield b

# res=disp1(10,20)
# print(res)
# print(type(res))
# res=list(res)
# print(res)
# print(type(res))

def fetch_in_batches(orders,batch_size):
    for i in range(0,len(orders),batch_size):
        yield orders[i:i+batch_size]

orders=[101,102,103,104,105,106,107,108,109]

for batch in fetch_in_batches(orders,3):
    print(f"Processing batch:{batch}")