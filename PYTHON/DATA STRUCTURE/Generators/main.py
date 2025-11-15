# GENERATORS

# Generator objects - generator objects are iterable, each generation it generate or spit out a new value
#         they generate a new value in each iteration      
from sys import getsizeof
# EX:
values = (x * 2 for x in range(10)) # Generator Object
for x in values:
    print(x)

# get the size of an object 'from sys import getsizeof'
values = (x * 2 for x in range(1000)) # even changed the range to higher the size still remain the same
print("gen:", getsizeof(values), "bytes") # output: gen: 200 bytes
