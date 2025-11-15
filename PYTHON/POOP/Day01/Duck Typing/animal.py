class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False
    
    def speak(self):
        print("HONK!")