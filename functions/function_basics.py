# Functions
# from email.utils import * # this line will make all functions inside the utils module (in the email  -
# # - package in current file
#
# import time
#
# # COMPANY = "Level up"
#
#
# # ================= Defining the functions ===========================
# def greet_user():
#     # for user
#     """ Greets the user."""
#     print("Welcome to the Class!")
#     print("this was basic function")
#
#
# def greet_user_1(name):
#     """Greeting the user with given name."""
#     print(f"Welcome to {name}!")
#
#
# def greet_user_2(company, username ):
#     """Greeting the user with given name."""
#     print(f"{username.title()}, Welcome to {company.upper()}!")
#     print("Have a great weak!")
#
#
#
# def greet_user_3(username, company="google"): # company argument is an optional argument, and default value is google
#     """Greeting the user with given username and keyword argument 'company'."""
#     print(f"{username.title()}, Welcome to {company.upper()}!")
#     print("Have a great weak!")
#
#
# def greet_user_4(username, company=None): # company argument (keyword), is an optional argument, and NO default value
#     """Greeting the user with given username and keyword argument 'company'."""
#     if company is None:
#         print(f"{username.title()}, Welcome to new home!")
#     else:
#         print(f"{username.title()}, Welcome to {company.upper()}!")
#     print("Have a great weak!")


# def add_inc(name):
#     print(f"your company name: {COMPANY}")
#     print(f"{name} Inc.")
#     #COMPANY = COMPANY + 'Inc.'

# # print ("Execution of functions")
# comp ='Level Up'
# greet_user() # this is the execution of the code inside the function >> calling the function
# time.sleep(5)
# greet_user_1(comp) # name parameter is required here, otherwise TypeError is thrown
# greet_user_1("Jungle") # name parameter is required here, otherwise TypeError is thrown
#
# print("Print statement")
#
# greet_user_1(input('enter company name: '))

# ======== package - directory with '__init__.py' empty file
# ========  Modules - '.py' file (python file)


# greet_user_2('Levelup', 'Rustem')
# greet_user_2('Rustem', 'LevelUP') # position is important here to print or do the execution correctly
#
# greet_user_3('Polina') # here function using default value for company argument, which was not provided in the call
# greet_user_3('Abdul', 'Facebook') # function overwrites the default 'google' value for the company argument
# greet_user_4('Vika') # company argument not used,  see the if condition in the function
# greet_user_4('Dilshod','Bloomberg')
# greet_user_4(company='Bloomberg', username='Dilshod')
# ===============================================================================================
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
#
# greet_user()
# ==================================================================================
# def greet_user(username):
#     """ Display a simple greeting."""
#     print("Hello," + username.title() + "!")
#
# greet_user('jesse') # you call greet many times:
# greet_user('sarah')
# ====================================================
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My" + animal_type +"'s name is " + pet_name.title() + ".")
#
# describe_pet(' German Shepherd', 'Julbars')# you can call a function the many times as needed.
# ============ HW chapter 8-1 ===================
# def display_message(username):
#     """ Display I'm learning Function py."""
#     print(" Hello I'm practicing function py " + username.title() + " !")
#
# display_message('sarah')



