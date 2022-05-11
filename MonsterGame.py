import monsters

level = 0

mon1 = monsters.Generator(4, "Fire").new()
mon2 = monsters.Generator(4, "Water").new()
mon3 = monsters.Generator(4, "Grass").new()

deck = [mon1, mon2, mon3]

def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    print(n1, "/", n2, "/", n3, "/", n4)
    print()


while True:
    level += 1
    print("----------------")
    print()
    ii = 1

    print("This is the deck you have:")
    for i in deck:
        print("Monster-" + str(ii) + ":")
        about(i)
        ii += 1
    print("")

    opponent = monsters.Generator(level).new()
    print("About your opponent:")
    about(opponent)

    while True:
        try:
            choice = int(input("Witch monster do you want to use? :"))
            print()
            pmon = deck[choice-1]
            break
        except:
            print("Wrong Input\n")

    ph = pmon.hp()
    pa = pmon.power()

    oh = opponent.hp()
    oa = opponent.power()

    h = 0
    while True:
        h += 1
        print("Round " + str(h))
        print()

        ph = ph - oa
        oh = oh - pa

        if ph < 0:
            win = False
            break

        if oh < 0:
            win = True
            break

        if oh < 0:
            if ph < 0:
                
                if ph < oh:
                    win = False

                if oh < ph:
                    win = True

        print("Player hp:", str(ph))
        print("opponent hp:", str(oh))
        input("Press ENTER ")
        print("------------")
        print()

    print("Score:", level)
    if win == True:
        print("You won this round!")

    if win == False:
        print("The opponent won!")
        break
    input("Press ENTER ")
    ii = 1
    
    print("This is the deck you have:")
    for i in deck:
        print("Monster-" + str(ii) + ":")
        about(i)
        ii += 1
    print("")

    while True:
        try:
            choice = int(input("Witch monster do you want to upgrade? :"))
            print()
            pmon = deck[choice-1]

            if choice == 1:
                mon1 = monsters.Upgrade(mon1).at
            if choice == 2:
                mon2 = monsters.Upgrade(mon2).at
            if choice == 3:
                mon3 = monsters.Upgrade(mon3).at

            break
        except:
            print("Wrong Input\n")
    print()


    

    