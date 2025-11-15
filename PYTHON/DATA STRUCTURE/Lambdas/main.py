# LAMBDAS EXPRESSION/FUNCTION


# SORTING A LIST OF TUPLES USING LAMBDA

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# USING LAMBDA EXPRESSION/FUNCTION items.sort(key=lambda parameters:expression)
items.sort(key=lambda item:item[1])
print(items)


