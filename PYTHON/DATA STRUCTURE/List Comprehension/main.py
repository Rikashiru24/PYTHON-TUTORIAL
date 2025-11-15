# LIST COMPREHENSION

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# get and iterate all the prices using list comprehension
# SYNTAX: [expression for item in items]
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 10]
print(filtered)
