import random

def get_die(sides=6):
    choices = range(1, sides +1)
    
    def roll():
        return random.choice(choices)
    return roll

d8 = get_die(8)

d20 = get_die(20)
print(d8(),d20())
