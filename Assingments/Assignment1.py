#convert the prices in USD & Euro using appropriate function
# PricesList_inr =[3000,56000,45000,2300]
# def us():
#     global PricesList_inr
#     usd=[]
#     for i in PricesList_inr:
#         usd.append(i*0.012)
#     return usd

# def eu():
#     global PricesList_inr
#     euro=[]
#     for i in PricesList_inr:
#         euro.append(i*0.011)
#     return euro
# print(f"inr {PricesList_inr} to usd:{us()}")
# print(f"inr {PricesList_inr} to usd:{eu()}")


# List the name which has more than 6 characters as lone_names list using appropriate function
# student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad","Samalla Akshay"]
# six_letter_list=list(filter(lambda x:len(x)>6,student_name_list))
# print(six_letter_list)


#Display the Product in ascending order based on the price of the product
# products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
# price_sort=sorted(products,key=lambda x:x["price"])
# print(price_sort)

# You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order
# lst=list(map(int,input("Enter the list of values:").split()))
# odd=list(filter(lambda x:x%2==0,lst))
# even=list(filter(lambda x:x%2==1,lst))
# for i in range(0,len(even)):
#     even[i] *=2
# lst.clear()
# lst=odd+even
# lst.sort()
# print(lst)
    
# You have a list of cities with their population data. Sort the cities in descending order of their population.
# cities = [
#     {"name": "New York", "population": 8419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]
# cities.sort(key=lambda x:x["population"],reverse=True)
# print(cities)

'''Extract Emails of Verified Users You have a list of user records with email and a verification status. 
 Extract the emails of verified users.'''
# users = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]
# verified_users=[user["email"] for user in users if user["verified"]==True]
# print(verified_users)

'''Calculate Discounts for Products You have a list of products with their prices. 
Apply a 20% discount to products costing more than $100 and return the updated prices.'''

# products = [
# {"name": "Laptop", "price": 1200},
# {"name": "Headphones", "price": 80},
# {"name": "Smartphone", "price": 700},
# {"name": "Monitor", "price": 150}
# ]

# disp=lambda x:(x-((x*20)/100))
# gr_price=list(filter(lambda x:x["price"]>100,products))
# for i in gr_price:
#     i["price"]=disp(i["price"])
# print(gr_price)

# sort Words by Length
words = ["apple", "banana", "cherry", "date", "fig"]
words.sort()
words.sort(key=lambda x:len(x))
print(words)

# write a program to remove the duplicates in the list
numbers=[2,2,4,6,3,4,6,1]
# st=set(numbers)
# numbers=list(st)
# print(numbers)
i=0
while i<len(numbers):
    if numbers.count(numbers[i])>1:
        numbers.remove(numbers[i])
    else:
        i +=1
print(numbers)