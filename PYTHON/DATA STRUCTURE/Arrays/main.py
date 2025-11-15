# ARRAYS
from array import array

# for documentation search google: 'python 3 typcode'
# note: the objects in this array are type (similar type only)

numbers = array("i", [1, 2, 3])

for number in numbers: # iterate items
    print(number)

numbers.append(4) # append/add item at the end of the array list
numbers.insert(2, 5) # insert item at the specified position
numbers.pop() # pop out the last item
numbers.remove(5) # remove specified item
print(numbers[0]) # accessed item using index
numbers[0] = 9 # modified specified index
print(numbers)
