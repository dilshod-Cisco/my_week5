# =======================  Classes - Chapter 9   =========================
# =======  Class - general template, where you have description and behaviour anything you want represents:
# ============ class name always starts with capital letter: =============


class Dog():
    """ This is the general class about Dog."""
    # ============= Attribute(properties) ================================

    breed = ''
    name = ''

    # == Behaviour, methods
    def bark(self):
        print("wouf wouf !!")

class NewDog():
    """ This is the new class aboute dog with mandatory parameters."""

    def __init__(self, name, age): # initiation/ constructor
        self.name = name
        self.age = age
        print("Constructing the New dog class.")

    # ============ Behaviour, methods ==========================
    def bark(self):
        print(f"{self.name} is barking:wouf wouf !!")

    def get_name(self):
        print(self.name)




# ====== Object is the instance of the class: this process is called instantiation
dog1 = Dog() #  ============ mydog is the object ( instance of the class) of Dog() class ===========
dog1.breed = 'German shepherd'
dog1.name = 'rex'
#dog1.bark() # ===========  this is "BARK()" accessing method of the class =============


dog2 = Dog()
dog2.name = "bobik"
dog2.breed = 'pudo'
#dog2.bark()

print('name of dog1', dog1.name)
print('name of dog1', dog1.breed)
dog1.bark()

print('name of dog2', dog2.name)
print('name of dog2', dog2.breed)
dog2.bark()


print("----------------------------")
dog3 = NewDog('sharik', 4)
dog3.bark()
dog3.get_name()

dog4 = NewDog('hatiko', 3)
dog4.bark()
dog4.get_name()
