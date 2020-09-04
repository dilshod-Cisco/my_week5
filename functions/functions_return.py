# Return value

def full_name(first, last):
    """Returns full name"""
    #print(f"{first.title()} {last.title()}")
    return f"{first.title()} {last.title()}" # "RETURN" keep the value in memory:

def adding(a, b):
    return a + b
# nums = [5, 55, 76, 1, -9, 0, 1, 456]
#
#
# total = adding(456, 987)
# print(f"Total is {adding(546, 987)}")



def full_name_dict(first: str, last: str) -> dict: # "DICT" return type: "STR" data type i'm excepting:
    """Returns dictionary with first_name, last_name"""
    result = {'first_name': first.title(), 'last_name': last.title()}
    return result

# public hashmap full_name_dict(String first, String last){ # JAVA way do this examples:(Type Language)
#    // JAVA code here, example of code, 1 of the reasons called type language:
# }
# ============ ==================== function return    ========================  ========================


full_name('anvar', 'nosirov')
name = full_name('john', 'doe')
print(f"{name}, Welcome to the class !")

total = adding(456, 987)
print(f"Total is {adding(546, 987)}")
student1 = full_name_dict('tatiana', 'shark')
print(student1)
print(student1['first_name'])

# == full_name_dict()
# ============= ==================== ===================== ===================

# def find_num(num_list, number):
#     for num in num_list:
#         if num == number:
#             print(f"{number} is found !!.")
#             break
#     else:
#         print(f"{number} is not found !! ")
#
#
# find_num(nums, 1)
# find_num(nums, 46)
# find_num([45, 0, 'hello'], 7)

# ======== ===========  ============ ============    ================  ===============

# def desc_pizza(*toppings):
#     print("We have only cheese pizza with following toppings: ")
#     print(*toppings)
#
# desc_pizza('chicken')
# desc_pizza('chicken', 'peperoni', 'bbq chicken')
# print('hello', 32, ['D', 'A'], 'world')























