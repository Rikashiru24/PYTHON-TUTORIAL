# ACCESSING ITEMS   

letters = ["a", "b", "c", "d"] # lists of strings
letters[0] = "A" # modified the item-assigned in the accessed index
print(letters)
print(letters[0]) # accessing the specified index and returns that item
print(letters[-1]) # returns last index item

# INDEX-SLICING
print(letters[0:3]) # returns the first 3 items in the original list
print(letters[:3]) # returns the first 3 items first args is zero by default
print(letters[::2]) # returns items by step 2 or every seconds from the orig list
print(letters[0:]) # returns original list

# ANOTHER EXAMPLE

numbers = list(range(20))
print(numbers[::2]) # return items in every second steps
print(numbers[::-1]) # return items in reversed orders
 
