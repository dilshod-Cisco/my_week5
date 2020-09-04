from classes.cars import Car, ElectricCar
# from classes.cars import *  # " this can import all"


car1 = Car('toyota', 'highlander', '2020')
print(car1.get_description())
car1.set_color('Red')
print(car1.get_description())
print(car1.read_odometer())

car1.odometer_reading = 1000
print(car1.read_odometer())
print(car1.odometer_reading)

#car1.odometer_reading = 800 # not good practice
car1.set_odometer(800)
print(car1.read_odometer()) # we can put logic in the method
print(car1.odometer_reading)

car1.set_odometer(1500)
print(car1.read_odometer())

car1.increment_odometer(-500)
print(car1.read_odometer())

car1.increment_odometer(400)
print(car1.read_odometer())
# ===========================================================

ecar1 = ElectricCar('Tesla', 'Model Y', '2020')
print(ecar1.get_description())
ecar1.set_color('Silver')
print(ecar1.get_description())
print('------------------------------')
ecar1.test_method()

# Object Oriented Programming
# - Class, Object
# - Inheritance (single class, multiple class)
# - Constructor (__init__() )
# - self keyword, super() method, difference
# - Overriding(due inheritance) - rewriting parent attributes/method in child class
# - check: JAVA method to overload, using the same name with different parameters
# - relationship between Parent and Child: Parent >> Child
# - parent does not have access to child attributes/method



