# MAP FUNCTION

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# Transform the list into numbers of list of prices

# here we have transformed or mapped our original list into a different list
prices = []
for item in items:
    prices.append(item[1])
print(prices)

# using map() function and lambda
x = map(lambda item:item[1], items)
for item in x:
    print(item)

# ALTERNATIVE: convert map object into list object
prices = list(map(lambda item:item[1], items))
print(prices)

