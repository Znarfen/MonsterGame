import monsters
import random
import time

#Print+
def say(a = "", b = "", c = "", d = ""):
    print(a, b, c, d)
    time.sleep(0.5)

def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    say(n1 + " / " + n2 + " / " + n3 + " / " + n4)
    say()

def game():
    mon1 = monsters.Generator(2, "Fire").new()
    mon2 = monsters.Generator(2, "Water").new()
    mon3 = monsters.Generator(2, "Grass").new()
    level = 0
    deck = [mon1, mon2, mon3]

    while True:
        
        level += 1
        say("----------------")
        say()
        ii = 1

        say("This is the deck you have:")
        for i in deck:
            say("Monster-" + str(ii) + ":")
            about(i)
            ii += 1
        say("")

        opponent = monsters.Generator(level * 4).new()
        say("About your opponent:")
        about(opponent)

        while True:
            try:
                choice = int(input("Witch monster do you want to use? :"))
                say()
                pmon = deck[choice-1]
                break
            except:
                say("Wrong Input\n")

        ph = pmon.hp()
        pa = monsters.Battle(pmon, opponent).attack()
        
        oh = opponent.hp()
        oa = monsters.Battle(opponent, pmon).attack()
        
        h = 0
        while True:
            h += 1
            say("Round " + str(h))
            say()

            r = random.randint(1, 20)
            if r == 1:
                say("Player: SUPER-DUPER-DUPER ATTACK")
                pa = pa + 4
            
            r = random.randint(1, 20)
            if r == 1:
                say("Opponent: SUPER-DUPER-DUPER ATTACK")
                oa = oa + 4

            ph = ph - oa
            oh = oh - pa

            say("Player attak:", pa, "/ Player hp:", ph)
            say("Opponernt attak:", oa, "/ Opponent hp:", oh)
            say()
                
            if oh or ph < 0:

                if ph < oh:
                    win = False
                    say(pmon.name() + " faild")
                    break

                if oh < ph:
                    win = True
                    say(opponent.name() + " faild")
                    break

            say()
            input("Press ENTER ")
            say("------------")
            say()

        say("Score: ", level)
        if win == True:
            say("You won!")
            input("Press ENTER")
            say()

        if win == False:
            say("The opponent won!")
            input("Press ENTER ")
            say()
            say("Your monster", pmon.name(), "is now ded!")
            say()
            deck.remove(deck[choice-1])
            if len(deck) == 0:
                say("All your monsters has ben defeted!")
                say()

                #name = input("Enter your name:")
                #f = open("Score.txt", "a")
                #f.write(name + "" + str(level) + "\n")
                #say()
                break
        
        ii = 1

        if win == True:
            say("This is the deck you have:")
            for i in deck:
                say("Monster-" + str(ii) + ":")
                about(i)
                ii += 1
            say("")

            while True:
                try:
                    choice1 = int(input("Witch monster do you want to upgrade? :"))
                    say()
                    pmon = deck[choice1-1]
                    deck.remove(pmon)
                    r = random.randint(0,1)

                    if r == 0:
                        if choice1 == 1:
                            mon1 = monsters.Upgrade(pmon).at()
                            deck.append(mon1)

                        if choice1 == 2:
                            mon2 = monsters.Upgrade(pmon).at()
                            deck.append(mon2)

                        if choice1 == 3:
                            mon3 = monsters.Upgrade(pmon).at()
                            deck.append(mon3)
                    
                    if r == 1:
                        if choice1 == 1:
                            mon1 = monsters.Upgrade(pmon).hp()
                            deck.append(mon1)

                        if choice1 == 2:
                            mon2 = monsters.Upgrade(pmon).hp()
                            deck.append(mon2)

                        if choice1 == 3:
                            mon3 = monsters.Upgrade(pmon).hp()
                            deck.append(mon3)

                    break
                except:
                    say("Wrong Input\n")

def main():
    while True:
        say("----------")
        say("1. PLAY")
        say("2. SETINGS")
        say("3. HARD MODE")
        say("----------")
        say()

        x = input(":")
        say()

        if x == "1":
            game()
        

main()