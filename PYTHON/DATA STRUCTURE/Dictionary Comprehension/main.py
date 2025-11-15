# DICTIONARY COMPREHENSION

# traditional loop over list
values = []
for x in range(5):
    values.append(x * 2)
    print(values)

# output: 
# [0]
# [0, 2]
# [0, 2, 4]
# [0, 2, 4, 6]
# [0, 2, 4, 6, 8]

#====================================

# list comprehension
values = [x * 2 for x in range(5)]
print(values) # output: [0, 2, 4, 6, 8]

# set comprehension
values = {x * 2 for x in range(5)}
print(values) # output: {0, 2, 4, 6, 8}

# using comprehension expression to create dictionary objects
# DICTIONARY COMPREHENSION
values = {x: x * 2 for x in range(5)}
print(values) # output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}