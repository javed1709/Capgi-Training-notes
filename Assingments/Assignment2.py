#frequency count of words in a sentence
map={}
products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
products=products.split(" ")
for i in products:
    if i not in map.keys():
        map[i]=1
    else:
        map[i] +=1
print(map.items())

#Store management
initial_stock = {"apple": 50,"banana": 100,"orange": 75}

sold_item = {"apple": 10, "banana": 20, "orange": 15}

for i in sold_item.keys():
    initial_stock[i]=initial_stock[i]-sold_item.get(i)
print(initial_stock)

# You have sales data for different regions and want to calculate the total sales for each region.
sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
total_sales={}
for i in sales_data:
    key,value=i["region"],i["sales"]
    if not(total_sales.get(i["region"],False)):
        total_sales[key]=value
    else:
        total_sales[key] +=value
           
for i in total_sales:
    print(f"sales in {i} region is {total_sales[i]}")


# mobile number in words
dc = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}
n = input("Enter the mobile number: ")
for i in n:
    print(dc[int(i)], end=" ")