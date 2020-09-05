# ===== HW 8-1 ===
# def display_message(username):
#     """ Display  a massage about what I'm Learning."""
#     msg = "I'm learning to store code in function. "
#     print(msg)
# display_message()

# === HW 8-2 =====

# def favorite_book(username):
#     """ Display a message about someone's favorite book."""
#     print(title + " is one of my favorite books. ")
#
# favorite_book('Napoleon Hill')

# === 8-3 ======================
# def make_shirt(size, message):
#     """ Summarize the shirt that's going to be made. """
#     print("\nI'm going to make a " + size + "t-shirt. ")
#     print('It will say, "' + message + '"')
#
# make_shirt('large', 'I love Python !')
# make_shirt(message = "Readability counts.", size = 'medium')
#
# # ====== 8-4 ==============
# def make_shirt(size = 'large', message = 'I love Python!'):
#     """ Summarize the shirt that's going to be made."""
#     print("\nI'm going to make a" + size + "t-shirt.")
#     print('It will say, "' + message + '"')
#
# make_shirt()
# make_shirt(size = 'medium')
# make_shirt('small', 'Python Awesome ^_^ ')

# ===== 8-5 ===============
# def describe_city(city, country = 'USA'):
#     """ Describe City."""
#     msg = city.title() + " is in " + country.title() + "."
#     print(msg)
#
# describe_city('brooklyn')
# describe_city('santa monica')
# describe_city('montreal', 'canada')
# describe_city('barcelona', 'spain')

# =========== 8-6 ================
# def city_country(city, country):
#     """ Return a string like 'Santiago, Chile'. """
#     return(city.title() + ", " + country.title())
#
# city = city_country('santiago', 'chile')
# print(city)
#
# city = city_country('buenos aires', 'argentina')
# print(city)
#
# city = city_country('bavaria', 'germany')
# print(city)

# =========== 8-7 ===================
# def make_album(artist, title):
#     """ Build a dictionary containing information about an album. """
#     album_dict = {
#         'artist': artist.title(),
#         'title' : title.title(),
#     }
#     return album_dict
#
# album = make_album('metallica', 'ride the light thing')
# print(album)
#
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)
# ----------------------------------------------------------------------------
# def make_album(artist, title, tracks = 0):
#     """ Build a dictionary containing information about an album. """
#     album_dict = {
#         'artist': artist.title(),
#         'title' : title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict
#
#
# album = make_album('metallica', 'ride the lightning')
# print(album)
#
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)
#
# album = make_album('iron maiden', 'piece of mind', tracks=8)
# print(album)

# ================= 8-8 ===============
# def make_album(artist, title, tracks=0):
#     """ Build a dictionary containing information about an album. """
#     album_dict = {
#         'artist': artist.title(),
#         'title' : title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict
#
#   #=== Prepare the prompts.
#
# title_prompt = "\nWhat album are you thinking of ?"
# artist_prompt = "Who's the artist ?"
#
#   # == Let the user know how to quit.
# print("Enter 'quit' at any time to stop. ")
#
# while True:
#     title = input(title_prompt)
#     if title == 'quit':
#         break
#
#     artist = input(artist_prompt)
#     if artist == 'quit' :
#         break
#
#     album = make_album(artist, title)
#     print(album)
#
# print("\nThanks for responding!")

# ================ 8-9 ===============
# def show_magicians(magicians):
#     """ Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician.title())
#
#
# magicians = [''Mike', 'David Copperfield ', 'Suzan ']
# show_magicians(magicians)

# ========== 8-10 ===================
# def show_magicians(magicians):
#     """ Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)
#
# def make_great(magicians):
#     """ Add 'the Great!' to each magician's name."""
#     # Build a new list to hold the great magicians.
#     great_magicians = []
#
#     # Make each magicians great, and add it to great_magicians.
#     while magicians:
#         magician = magicians.pop() # removes 'pop()'
#         great_magician = magician + 'the Great'
#         great_magicians.append(great_magician) # 'append' adds elements on the list!
#
#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magicians.append(great_magician)
#
# magicians = ['Mike', 'David Copperfield ', 'Suzan ']
# show_magicians(magicians)
#
# print("\n")
# make_great(magicians)
# show_magicians(magicians)

# ==== 8-11 =================
# def show_magicians(magicians):
#     """ Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)
#
#
# def make_great(magicians):
#     """ Add 'the Great!' to each magician's name."""
#     # Build a new list to hold the great magicians.
#     great_magicians = []
#
#     # Make each magician great, and add it to great_magicians.
#     while magicians: # 'while' loop !
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#
#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magicians.append(great_magician)
#
#     return magicians
#
# magicians = ['Mike', 'David Copperfield ', 'Suzan ']
# show_magicians(magicians)
#
# print("\nGreat magicians:")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)
#
# print("\nOriginal magicians:")
# show_magicians(great_magicians)
#
# print("\nOriginal magicians:")
# show_magicians(magicians)

# ============ 8-12 ============
# def make_sandwich(*items):
#     """ Make a sandwich with the given Items."""
#     print("\nI'll make you a great sandwich: ")
#     for item in items:
#         print("  .... adding" + item + "to your sandwich.")
#     print("Your sandwich is ready !")
#
# make_sandwich('roast beef', 'chedar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slice', 'honey mustard',)
# make_sandwich('peanut butter', 'strawberry jam')

# ========= 8-13 =============

# ========== 8-14 =============
#    # car = make_car('Lexus', 'Outback', color='black', tow_package=True)
#
# def make_car(manufacturer, model, **options):
#     """" Make a dictionary representing a car."""
#     car_dict = {
#         'manufacturer' : manufacturer.title(),
#         'model' : model.title(),
#
#         }
#     for option, value in options.items():
#         car_dict[option] = value
#
#     return car_dict
#
# my_outback = make_car('lexus', 'outback', color='black', tow_package=True)
# print(my_outback)
#
# my_bmw = make_car('bmw', 'm3', year=2020, color='white', headlights='popup')
# print(my_bmw)

# ========== 8-15 =================
# """ Functions related to printing 3d models."""
#
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until there are none left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # Simulate creating a 3d print from the design.
#         print("Printing model:" + current_design)
#
# def show_completed_models(completed_models):
#     """ Show all the models that where printed. """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)



# ==== youshould use import here form different list ok? { printing_models.py:

# import printing_function as pf
# unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# pf.print_models(unprinted_design, completed_models)
# pf.show_completed_models(completed_models)









































