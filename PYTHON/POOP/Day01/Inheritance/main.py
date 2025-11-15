# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

from animal import Dog, Cat, Mouse

dog = Dog("Scooby")

cat = Cat("Garfield")

mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
mouse.speak()