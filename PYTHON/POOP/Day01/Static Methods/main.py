# Static methods = A method that belong to a class rather than any object from that class (instance)
#                   Usually used for general utility functions

# Instance methods = Best for generations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


print(Employee.is_valid_position("Manager"))

employee1 = Employee("Spongebob", "Cook")
print(employee1.get_info())