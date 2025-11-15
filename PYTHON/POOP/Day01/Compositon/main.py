# Composition = The composed object directly owns its components, which cannot exist independently
#               "owns-a" relationship

from engine import Engine, Wheel, Car

car = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)

print(car.display_car())