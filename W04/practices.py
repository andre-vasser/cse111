import random

def get_die(sides=6):
    choices = range(1, sides +1)
    return random.choice(choices)

print(get_die())
