# LOOPING OVER LIST

letters = ["a", "b", "c"]

# using for-loop to loop over the list
for letter in letters:
    print(letter)

# if to get index of each item as well use 'enumerate()' function
for letter in enumerate(letters):
    print(letter) # this will give us a tuple

# to get the index and item in tuple
for letter in enumerate(letters):
    print(letter[0], letter[1]) # return the index and the item

# another way to get index and item without tuple results, that is unpacking
# I call this "Unpacking tuple results in for-loop"
for index, letter in enumerate(letters):
    print(index, letter)

