import monsters
import random

level = 0

mon1 = monsters.Generator(2, "Fire").new()
mon2 = monsters.Generator(2, "Water").new()
mon3 = monsters.Generator(2, "Grass").new()

def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    print(n1, "/", n2, "/", n3, "/", n4)
    print()

def main():
    print()
    print("1. PLAY")
    print("2. HOW TO PLAY")
    print("3. SETINGS")
    print("4. HIGH SCORE")



def game():
    while True:
        deck = [mon1, mon2, mon3]

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
        pa = monsters.Battle(pmon, opponent).attack()
        
        oh = opponent.hp()
        oa = monsters.Battle(opponent, pmon).attack()
        
        h = 0
        while True:
            h += 1
            print("Round " + str(h))
            print()

            r = random.randint(1, 20)
            if r == 1:
                print("Player: SUPER-DUPER-DUPER ATTACK")
                pa = pa + 4
            
            r = random.randint(1, 20)
            if r == 1:
                print("Opponent: SUPER-DUPER-DUPER ATTACK")
                oa = oa + 4

            ph = ph - oa
            oh = oh - pa

            print("Player attak:", pa, "/ Player hp:", ph)
            print("Opponernt attak:", oa, "/ Opponent hp:", oh)
            print()

            if ph < 0:
                win = False
                print(pmon.name(), "faild")
                break

            if oh < 0:
                win = True
                print(opponent.name(), "faild")
                break
                
            if oh < 0:
                if ph < 0:
                    
                    if ph < oh:
                        win = False
                    if oh < ph:
                        win = True
                    break

            print()
            input("Press ENTER ")
            print("------------")
            print()

        print("Score:", level)
        if win == True:
            print("You won!")

        if win == False:
            print("The opponent won!")
            break
        print()
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
                choice1 = int(input("Witch monster do you want to upgrade? :"))
                print()
                pmon = deck[choice1-1]
                r = random.randint(0,1)

                if r == 0:
                    if choice1 == 1:
                        mon1 = monsters.Upgrade(mon1).at()

                    if choice1 == 2:
                        mon2 = monsters.Upgrade(mon2).at()

                    if choice1 == 3:
                        mon3 = monsters.Upgrade(mon3).at()
                
                if r == 1:
                    if choice1 == 1:
                        mon1 = monsters.Upgrade(mon1).hp()

                    if choice1 == 2:
                        mon2 = monsters.Upgrade(mon2).hp()

                    if choice1 == 3:
                        mon3 = monsters.Upgrade(mon3).hp()

                break
            except:
                print("Wrong Input\n")
        print()


    

    