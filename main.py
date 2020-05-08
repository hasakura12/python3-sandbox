# use pyenv to manage version
# curl https://pyenv.run | bash
# pyenv install -l
# pyenv install -v 3.8.2

# install required packages to virtualenv (local to app)
# pip install virtualenv
# virtualenv venv
# sudo chmod 744 venv/bin/activate
# source venv/bin/activate
# pip install -r requirements.txt

import json

# To get current date and time we need to use the datetime library
from datetime import datetime, timedelta
import pprint

# import module as namespace (i.e. requires prepending namespace like helpers.method())
import helpers
# import all into current namespace (i.e. NOT required to prepending namespace, just call method())
# from helpers import *
# from helpers import display


def print_var():
    first_name = "first"
    last_name = "last"
    output = "Hello " + first_name + " " + last_name
    print(output)

    # python 3 syntax
    output2 = f"Printing with python3 syntax... {first_name} {last_name}"
    print(output2)

def print_date():
    today = datetime.now()
    print("Today is: " + str(today))

    #You can use timedelta to add or remove days, or weeks to a date
    one_day = timedelta(days=1)
    yesterday = today - one_day
    print("Yesterday was: " + str(yesterday))

def error_handle_example():
    x = 5
    y = 0
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print("Not allowed to divive by 0")
    else:
        print("Something else went wrong")
    finally:
        print("this is cleanup")

def print_array():
    animals = ["dog", "cat", "bird", "fish"]
    print(f"Here are all the animals: {animals}")

    if animals[0] == animals[1]:
        print(f"{animals[0]} and {animals[1]} are the same")
    else:
        print(f"{animals[0]} and {animals[1]} are NOT the same")

    print("looping through array declaretively...")
    for animal in animals:
        if animal == "fish":
            print(f"    {animal} is FISH!")
        else:
            print(f"    {animal} is NOT FISH!")

    print("looping through array iteratively...")
    for i in range(0, len(animals)):
        if animals[i] == "fish":
            print(f"    {animals[i]} is FISH!")
        else:
            print(f"    {animals[i]} is NOT FISH!")

def print_map():
    # from python > 3.6, dict is ordered
    petsMap = {}
    petsMap["dog"] = "true"
    petsMap["cat"] = "true"
    petsMap["bird"] = "true"
    print(f"petsMap: {petsMap}")
    print(f"petsMap using json: {json.dumps(petsMap)}") # convert map to json and print it ou

    animalMap = {}
    animalMap["pets"] = petsMap
    print(f"animalMap: {animalMap}")
    print(f"animalMap using json: {json.dumps(animalMap)}")
    print(f"is cat a pet? {animalMap['pets']['cat']}")

    print("looping through map declaretively...")
    for key, value in animalMap.items():
        print(f"    ({key}, {value})")

def init_list_of_map() -> []:
    employees = []
    employee = {}
    employee["first_name"] = "joe"
    employee["last_name"] = "doe"
    employee["age"] = "12"
    employees.append(employee)

    employee = {}
    employee["first_name"] = "john"
    employee["last_name"] = "smith"
    employee["age"] = "32"
    employees.append(employee)

    employee = {}
    employee["first_name"] = "arthur"
    employee["last_name"] = "king"
    employee["age"] = "42"
    employees.append(employee)

    return employees

def print_list_of_maps():
    # list of map
    
    employees = init_list_of_map()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(f"employees: {employees}")

    print("looping through list of maps declaretively...")
    for employee in employees:
        if employee["first_name"] == "john":
            print(f"    {employee} is john!")
        else:
            print(f"    {employee} is NOT john!")


def reverse(list):
    start = 0
    end = len(list) - 1

    while start < end:
        tmp = list[start]
        list[start] = list[end]
        list[end] = tmp
        start += 1
        end -= 1

    return list


# decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
def decorator(func):
    def wrapper():
        print("before the function is called.")
        func()
        print("after the function is called.")
    return wrapper

# decorator call anotated by @
@decorator
def hello_world_decorator():
    print("HELLO WORLD")

# doc string & type hint example
def docstring_typehint(name: str) -> str:
    """
    Returns a string

    Parameter: name(str)
    Returns: string printed
    """

    print(f"docstring_typehint {name}")


# sorter for first name
def first_name_sorter(items: []) -> str:
    return items["first_name"]


print()
print("~WORKING ON VAR...")
print_var()

####################
## date           ##
####################
print()
print("~WORKING ON DATE...")
print_date()

####################
## error handling ##
####################
print()
print("~WORKING ON ERROR HANDLING...")
error_handle_example()

####################
## if / else  ##
####################
# array
print()
print("~WORKING ON ARRAY...")
print_array()

print("reversing list...")
animals = ["dog", "cat", "bird", "fish"]
reversed = reverse(list=animals) # can use named parameter
print(f"reversed animals: {reversed}")

print()
print("~WORKING ON MAP...")
print_map()


print()
print("~WORKING ON LIST OF MAPS...")
print_list_of_maps()


print()
print("~WORKING ON DECORATOR...")
hello_world_decorator()

print()
print("~WORKING ON SORTING...")
employees = init_list_of_map()
print(f"original employees: {employees}")

employees.sort(key=first_name_sorter)
print(f"sorted by first name of employees: {employees}")

# using lambda
employees.sort(key=lambda items: items["last_name"])
print(f"sorted by last name of employees: {employees}")

employees.sort(key=lambda items: items["age"])
print(f"sorted by age of employees: {employees}")
