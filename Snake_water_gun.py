import random

'''
                computer
             S W G
             0 1 2
user    S 0  D W L
        W 1  L D W
        G 2  W L D
'''

while True:
    print("\n0. Snake\n1. Water\n2. Gun\nq. Exit")
    user = input("$ > ")
    print()
    
    try:
        if user == 'q':
            break

        user = int(user)
        if user > 2 or user<0:
            print("Wrong Input !!")
            continue

    except Exception:
        print("Wrong Input !!")
        continue


    com = random.randint(0,2)
    # print(com)


    if user == com:
        print("Draw !!!")

    elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
        print("WON !!!")

    elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1):
        print("LOSE !!!")

print("Thanks for playing")