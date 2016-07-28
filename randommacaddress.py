#!/usr/env/python
#
# !/.scripts/alpha
#
# This script gets a random hex mac address 

import random

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def get_random_char(num_chars=1):
    global chars
    characters = ''
    for i in range(num_chars):
        characters += chars[random.randrange(0, 16)]
    return characters

def get_random_address():
    address = ''
    for i in range(5):
        address += get_random_char(2)
        address += ':'
    address += get_random_char(2)
    return address

print(get_random_address())
