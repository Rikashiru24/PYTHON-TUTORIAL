class Car:

    def __init__(self, speed=0, color="unknown"):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value
    
    def get_speed(self):
        return print(f"{self.__speed} kmp/h")
    
    def set_color(self, paint):
        self.__color = paint

    def get_color(self):
        return print(f"Painted '{self.__color}'")


lamborghini = Car()
lamborghini.get_speed()
lamborghini.set_speed(3)
lamborghini.set_color("Pink")
lamborghini.get_color()



