# SORTING LISTS

numbers = [3, 51, 2, 8, 6]
numbers.sort() # sorted in ASCENDING order
print(numbers)

# to sort in DESCENDING order sort(key, reverse) takes two parameters
numbers.sort(reverse=True)
print(numbers)

# using BUILT-IN Functions sorted(iterable, key, reverse)
print(sorted(numbers)) # returns new list and not modified
print(sorted(numbers, reverse=True)) # reverse sort

print()

# SORTING A LIST OF TUPLES

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# define a function to sort it
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
