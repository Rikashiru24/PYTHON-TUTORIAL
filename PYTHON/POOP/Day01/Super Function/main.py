# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

from shapes import Circle, Square, Triangle

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
print(f"{circle.color} {circle.is_filled} {circle.radius}cm")

square.describe()
print(f"{square.color} {square.is_filled} {square.width}cm")

square.describe()
print(f"{triangle.color} {triangle.is_filled} {triangle.width}cm {triangle.height}cm")