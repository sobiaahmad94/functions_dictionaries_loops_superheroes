def return_10():
    return 10

def add(first_number, second_number):
    plus_sum_of_numbers = first_number + second_number
    return plus_sum_of_numbers

def subtract(first_number, second_number):
    subtract_sum_of_numbers = first_number - second_number
    return subtract_sum_of_numbers

def multiply(first_number, second_number):
    multiply_sum_of_numbers = first_number * second_number
    return multiply_sum_of_numbers

def divide(first_number, second_number):
    divide_sum_of_numbers = first_number / second_number
    return divide_sum_of_numbers

def length_of_string(test_string):
    length_of_string_calc = len(test_string)
    return length_of_string_calc

# print(length_of_string("yoyo"))

def join_string(string_1, string_2):
    strings_added_mary_song = string_1 + string_2
    return strings_added_mary_song

# print(join_string("Mary had a little lamb, ", "its fleece was white as snow"))

def add_string_as_number(string_1, string_2):
    plus_string_to_number_result = int(string_1) + int(string_2)
    return plus_string_to_number_result

# print(add_string_as_number("1", "2"))

def number_to_full_month_name(month_number):
    months_of_the_year = [
        {"month_name" : "January", "month_num" : 1},
        {"month_name" : "March", "month_num" : 3},
        {"month_name" : "September", "month_num" : 9}
    ]

    for month in months_of_the_year:
        if month["month_num"] == month_number:
            return month["month_name"]

def number_to_short_month_name(month_number): # user input
    months_calendar = [ # list
        {"month_num" : "1", "short_month_name" : "Jan"}, # dict
        {"month_num" : "4", "short_month_name" : "Apr"},
        {"month_num" : "10", "short_month_name" : "Oct"}
    ]

    for month in months_calendar: # month represents each iteration
        if month["month_num"] == str(month_number): # checking to see if the value against "month_num" key matches value user has given
            return month["short_month_name"] # if that's true ^ then "first_month_string" key's value returned

# In hindsight, I should've kept the month_num key values as ints not strings but instead I converted them which I didn't need to
# print(number_to_short_month_name(10))

# My examples
#----------------------
def get_superhero_alias(super_name):
    superheroes_book = [
        {"superhero_name" : "Spider-Man", "alias_name" : "Peter Parker"},
        {"superhero_name" : "Iron Man", "alias_name" : "Tony Stark"},
        {"superhero_name" : "Batman", "alias_name" : "Bruce Wayne"}
    ]

    for superhero in superheroes_book:
        if superhero["superhero_name"] == super_name:
            return superhero["alias_name"]

# print(get_superhero_alias("Spider-Man"))

#---------------------- 


def get_superhero_superpowers(superhero_name):
    superheroes_list = [
        {"name_of_superhero": "Spider-Man", "superpowers" : "spidey senses super strength climbing tall skyscraper buildings"}

    ]

    for superhero in superheroes_list:
        if superhero["name_of_superhero"] == superhero_name:
            return superhero["superpowers"]
    
# print(get_superhero_superpowers("Spider-Man"))
# ---------------------
# Refactor so that the superpowers can be stored within a list

# I will add some more examples to this 

    
    










