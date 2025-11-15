# FINDING ITEMS IN THE LIST

letters = ["a", "b", "c"]
print(letters.count("b")) # the return the number of occurences of the given item in list

print(letters.index("a")) # finds and return the index of the item in the list

# No 'ValueError' returns when object is not in the list
if "d" in letters:
    print(letters.index("d"))