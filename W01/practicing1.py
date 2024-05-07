import math
side = input side("Enter Area: ")

def calc_area_of_square(side):
    area = side **2
    print(area)

#variable assignment
abc = int(input('Whats the side of your quare?   '))

#variable assingment from the result (output) of a function
#calling/invoke
area = calc_area_of_square(abc)
    
#Example 2
def add_to_roster(r):
    while True:
        name = input('Please give me the name to add to the roster:  ')
        if name =='':
            break
        r.append(name)

roster =[]
add_to_roster(roster)

print (roster)