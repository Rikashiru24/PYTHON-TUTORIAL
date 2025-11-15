# Multiple Inheritance = Inherit from more than one parent class
#                        C(A, B)
# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
from animal import Rabbit, Hawk, Fish

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
