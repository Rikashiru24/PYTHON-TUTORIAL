# SWAPPING VARIABLES
x = 10
y = 11

x, y = y, x # turn into tuple because of comma
x, y = (11, 10) # is equivalent to this syntax. We're unpacking tuple, setting x=11 and y=10

print("x", x) # output: x 11
print("y", y) # output: y 10

