from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/")

db=client["database"]

collection=db["users"]

# print("Connected to Mongo Script")

user={"name":"John Doe","age":30,"city":"New York"}

# insert_result=collection.insert_one(user)

# print(f"Inserted ID: {insert_result.inserted_id}")

multiusers=[
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 28, "city": "Chicago"}
]

insert_many_results=collection.insert_many(multiusers)

# for user in collection.find():
#     print(user)

# for user in collection.find({"city":"New York"}):
#     print(user)

singleuser = collection.find_one({"name": "Alice"})  # finding user by name
print(singleuser)

collection.update_one({"name":"John Doe"},{"$set":{"age":31}})

for user in collection.find():
    print(user)

collection.update_many({"city":"New York"},{"$set":{"city":"LA"}})

for user in collection.find():
    print(user)

collection.delete_many({"name":"Alice"})

for user in collection.find():
    print(user)

# collection.delete_many({"age":{"$lt":30}}) #lt means <=30
print("lol")
for user in collection.find():
    print(user)

# collection.drop()
# print("Collection droped")