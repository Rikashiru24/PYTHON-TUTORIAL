# DICTIONARIES collections of key:value pairs

point1 = {"x": 1, "y": 2}
print(point1)
# using dict(key=value)
point = dict(x=3, y=4)
print(point)
print(point["x"]) # accessing value of key using name of a key
point["x"] = 10 # change the value of "x"
print(point) # output: {'x': 10, 'y': 4}
point["z"] = 5 # adding a new key:value
print(point) # output: {'x': 10, 'y': 4, 'z': 5}

#SOLUTIONT1: avoiding 'KeyError' when finding a key that is not in the dictonary
if "a" in point:
    print(point["a"]) # show no error

#SOLUTION2: using get() method
print(point.get("a")) # output: 'None'
print(point.get("a", 0)) # return '0' by default

# DELETE AN ITEM USING 'del'
del point["x"]
print(point) # output: {'y': 4, 'z': 5}

# LOOP OVER DICTIONARIES
# SOLUTION1: 
for key in point:
    print(key, point[key]) # output: y 4
#                                    z 5

#SOLUTION2:
for key, value in point.items(): # loop while unpacking
    print(key, value) # output: y 4
#                               z 5



