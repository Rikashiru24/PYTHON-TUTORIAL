# UNPACKING OPERATOR, unpack any iterable basically mean we take individual values

numbers = [1, 2, 3]
# using '*' to unpack
# takes out its individual elements and pass them as arbitrary arguments to the print function
print(*numbers) # output: 1 2 3

# Ex
values = list(range(5))
print(values) # output: [0, 1, 2, 3, 4]
values = [*range(5), *"Hello"]
print(values) # output: [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# combine multiple list
first = [1, 2]
second = [3]
combined = [*first, *second]
print(combined) # output: [1, 2, 3]

# UNPACK DICTIONARIES using '**' two asterisk

una = {"x": 1}
sunod = {"x": 10, "y": 2}
combine = {**una, **sunod}
print(combine) # output: {'x': 10, 'y': 2}, NOTICE 'x' became 10, because it will used the last value of the same 'key'
