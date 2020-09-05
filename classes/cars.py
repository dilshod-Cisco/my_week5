
class Car():
    """ This is class to represents car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = 'White'
        self.odometer_reading = 0 # in miles

    # ====  getter(return) and setter(assign a new value, method with parameter)
    def get_description(self):
        msg = f"Your car: \n\tmanufacturer: {self.make}, \n\tmodel: {self.model}\n\tYear: {self.year} \n\tColor: {self.color}"
        return msg



    def set_color(self, new_color):
        print(f"Changing the color {self.color} to {new_color}")
        self.color = new_color
        

    def read_odometer(self):
        """ Gets the odometer miles of the car."""
        msg = f" Car has {self.odometer_reading} miles on it."
        return msg

    def set_odometer(self, new_miles):
        if new_miles >= self.odometer_reading:
            print(f"Setting odometer reading from {self.odometer_reading} to {new_miles}")
            self.odometer_reading = new_miles
        else:
            print(f" You can not roll back odometer from {self.odometer_reading} to {new_miles}")

    def increment_odometer(self, miles):
        """ Adding :parameters miles to odometer_reading"""

        #self.odometer_reading = self.odometer_reading + miles
        if miles > 0:
            print(f"Incrementing odometer with more {miles} miles ")

            self.odometer_reading += miles # this 2 ^ lines identical:
        else:
            print(f"Negative value can not be passed to odometer : {miles}.")
# ================================================================================
class ElectricCar(Car): # Inheritting Car class
    """Represents Elecric car, inherits all features of Car."""

    def __init__(self, make, model, year):
        """ constructor can be different here,  OVERRIDING the parent constructor( child class constructor)"""
        super().__init__(make, model, year)# calling the constructor of parent class

        # self.make = make
        # self.model = model
        self.battery_size = 80
        # self.year = year
        # self.color = 'black'

    def get_description(self): # OVERRIDING the parent method !
        msg = f"Your car: \n\tmanufacturer: {self.make}, \n\tmodel: {self.model}\n\t"\
         f" Year:{self.year} \n\tColor: {self.color} \n\tBattery size: {self.battery_size}"
        return msg


    def test_method(self):
        print(self.get_description())  # current class get_description() method : with battery_size
        print(super().get_description())  # parent class get_description() method:

#  " 'this.get_description()' keyword in JAVA is used as  'self.get_description' in PYTHON " == current method====
# JAVA has a same thing like super().get_description() === parent method :



class Shape():

    @classmethod
    def area(self):
        pass

    @classmethod
    def perimetr(self):
        pass




class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.height *self.base


