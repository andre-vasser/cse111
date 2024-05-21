import random

def get_die():
       
    def roll():
        return range(random.choice(1, sides +1))
    return roll

d8 = get_die(8)

d20 = get_die(20)
print(d8(),d20())
