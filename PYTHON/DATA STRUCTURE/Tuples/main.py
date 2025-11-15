# TUPLES a read-only list

point1 = (1, 2, 3) # tuple
point2 = 1, 2, 3 # still a tuple even parenthesis is excluded
point3 = 1, # still a tuple as long as ther is a trailing comma ","
point4 = () # use empty parenthesis if defining a tuple
print(type(point1)) # output: <class 'tuple'>
print(type(point2)) # output: <class 'tuple'>
print(type(point3)) # output: <class 'tuple'>
print(type(point4)) # output: <class 'tuple'>

# CONCATENATE TUPLES
point5 = (1,2) + (3,4)
print(point5) # output: (1, 2, 3, 4)

# Multiplication operator to repeat a tuple
point6 = (1, 2) * 3 
print(point6) # output: (1, 2, 1, 2, 1, 2)

# convert a list into a tuple using tuple() function
point7 = tuple([1, 2])
print(point7) # output: (1, 2)

# string can be tuple as well, because it is iterable, using tuple() function
point8 = tuple("Hello World")
print(point8) # output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# accessing individual item using index like list
point9 = (1, 2, 3)
print(point9[0]) # output: 1
print(point9[0:2]) # output: (1, 2); 3 was not included because 2 is exclusive [start:end]

# Unpacking tuple
point10 = (1, 2, 3)
x, y, z = point10
print(x, y, z) # output: 1 2 3

if 10 in point10: # using in operator to check the existence of an item
    print("exist")
else:
    print("None")






