def add_to_roster(r):
    while True:
        name = input('Please give me the name to add to the roster:  ')
        if name =='':
            break
        r.append(name)


def main():
    roster=[]
    add_to_roster(roster)

if __name__ == '__main__':
     main()
     
    