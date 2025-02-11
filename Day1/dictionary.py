customer={
    "name":"Shaik Javed",
    "email": "javed1709@gmail.com",
    "phone":7965,
    "age":23,
    "is_verified":True
}
print(customer["name"])

#accesing the items using the get method
print(customer.get("name"))
#using get method if key does not exist then it will create a new pair in dictionary
print(customer.get("birthday","17-09-2002"))
print(customer.keys()) #list [] of keys returned
print(customer.values()) #list [] of values returned

# modify the value
customer["name"]="Javed"
print(customer.get("name"))