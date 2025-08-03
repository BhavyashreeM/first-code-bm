# Write code below 💖

import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']


# function 1
def capitalize_suffix(name):
    return name.capitalize()


capital_name = list(map(capitalize_suffix, suffixes))


# print(list(capital_name))

# Function 2 - given

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)


# list Comprehension
random_names = [create_fantasy_name(prefixes, capital_name) for name in range(10)]


#
def fire_in_name(name):
    return 'Fire' in name


filtered_name = list(filter(fire_in_name, random_names))


# concatenate
def concatenate_names(acc, name):
    return acc + ', ' + name


# reduce function
from functools import reduce

reduced_names = reduce(concatenate_names, filtered_name)


# Final Display function
def display_name_info():
    print('Fantasy Names: ')
    for name in random_names:
        print(name)
    print()
    print('Filtered Names :', filtered_name)
    print('Reduced Names :', reduced_names)


display_name_info()

