def add_to_roster(r):
    while True:
        name = input('Please give me the name to add to the roster:  ')
        if name =='':
            break
        r.append(name)

roster =[]
add_to_roster(roster)

print (roster)