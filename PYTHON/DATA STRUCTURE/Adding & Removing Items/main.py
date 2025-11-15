# ADDING/REMOVING ITEMS

letters = ["a", "b", "b", "c"]

# ADD
letters.append("d") # Add item at last position using function append() 
letters.insert(0, "-") # Add item at the specific position

# REMOVE
letters.pop() # remove the last item
letters.pop(0) # remove item at the given index
letters.remove("b") # remove the first occurence of item that you don't know the index
del letters[0:3] # remove a range of items
letters.clear() # delete all objects in the list
print(letters)


