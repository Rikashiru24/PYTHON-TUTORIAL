# Get individual items in the list and assigned them to different variables

# Example
numbers = [1,2,3,4,5,6,7,8,9]
# List Unpacking Syntax 1
# first, second, third = numbers
# print(first, second, third)

# List Unpacking Syntax 2
first, second, *other = numbers # the '*other' is packing all the other items into separate list
print(first, second, other) # return first[0], second[1] and list of other

# List Unpacking Syntax 3
# What if we only need to get the first and last items
first, *other, last = numbers # Move '*other' in between the first and last
print(first, last, other)


# List Unpacking Syntax Manual
first = numbers[0]
second = numbers[1]
third = numbers[2]
