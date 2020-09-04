# ex ===== 9-1 ======

class Restaurant():
    """ This class to represent Restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def get_description(self):
        msg = f" Today we open: special lunch:  name : {self.restaurant_name}, type: {self.cuisine_type} "
        return msg