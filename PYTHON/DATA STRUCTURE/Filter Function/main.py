# FILTER FUNCTION

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# Only get the 'price >= 10' (dollars), using built-in function 'filter()'
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

