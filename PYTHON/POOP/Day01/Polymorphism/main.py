# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from shape import Square, Circle, Triangle, Pizza

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Hawaiian", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")