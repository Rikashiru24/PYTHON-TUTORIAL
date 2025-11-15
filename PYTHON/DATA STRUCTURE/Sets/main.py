# SETS (a collection with no duplicates): Unordered Collections, cannot access using an index

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers) # transform into a set with no duplication
second = {1, 4} # creating a set of item
second.add(5) # append 5 to the last position
second.remove(5) # remove 5
third = len(second) # count the items
print(second)
print(third)
print(uniques)

# SETS MATHEMATICAL OPERATION
first = set(numbers)
seconds = {1, 5}

# UNION OF TWO-SETS using VERTICAL BAR '|'
# returns a new sets of items that are either in 'first' or 'seconds'
print(first | seconds) # output: {1, 2, 3, 4, 5}
# getting the intersection (returns items that are in both sets) of two sets
print(first & seconds) # output: {1}
# getting the difference (sets that don't have in the second set) between two sets
print(first - seconds) # output: {2, 3, 4}
# semantic difference, returns items in either sets but not both or similar
print(first ^ seconds) # output: {2, 3, 4, 5}
# checking the existence of an item in a set
if 1 in first:
    print("Yes")

