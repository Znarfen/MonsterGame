from re import A
import monsters
import random
import time

#Print+
def say(a = "", b = "", c = "", d = ""):
    print(a, b, c, d)
    time.sleep(0.2)

def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    say(n1 + " / " + n2 + " / " + n3 + " / " + n4)
    say()

def showdeck(deck):
    say("This is the deck you have:")
    ii = 1
    for i in deck:
        say(str(ii) + ". " + "Monster-" + str(ii) + ":")
        say(str(ii) + ". " + " Monster-" + str(ii) + ":")
        about(i)
        ii += 1
    say("")

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
        
        showdeck(deck)

        opponent = monsters.Generator(level).new()
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
        oh = opponent.hp()
        
        h = 0
        while True:
            pa = monsters.Battle(pmon, opponent).attack()
            oa = monsters.Battle(opponent, pmon).attack()

            rpa = pmon.power()
            roa = opponent.power()

            h += 1
            say("Round " + str(h))
            say()

            pb = pa - rpa
            ob = oa - roa

            if pb >= 0:
                pb = "+" + str(pb)
            if ob >= 0:
                ob = "+" + str(ob)

            pa2 = str(rpa) + " + (" + str(pb) + ")"
            oa2 = str(roa) + " + (" + str(ob) + ")"

            say("Before:")
            say("Player attak:", pa2, "/ Player hp:", ph)
            say("Opponernt attak:", oa2, "/ Opponent hp:", oh)
            say()

            ph = ph - oa
            oh = oh - pa

            say("After:")
            say("Player attak:", pa2, "/ Player hp:", ph)
            say("Opponernt attak:", oa2, "/ Opponent hp:", oh)
            say()

            if (0 >= oh) or (0 >= ph):

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

        say("Score:", level)
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
                input("Press ENTER ")
                
<<<<<<< HEAD
=======
                #Fill hantering FIXA

                #name = input("Enter your name:")
                #f = open("Score.txt", "a")
                #f.write(name + "" + str(level) + "\n")
                #say()
>>>>>>> 138d518599ce5b7c1c6a18dec8d3eaf0c0c4bc30
                break

        say()
        
        ii = 1

        if win == True:
            showdeck(deck)

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
                            deck.insert(0, mon1)

                        if choice1 == 2:
                            mon2 = monsters.Upgrade(pmon).at()
                            deck.insert(1, mon2)

                        if choice1 == 3:
                            mon3 = monsters.Upgrade(pmon).at()
                            deck.insert(2, mon3)
                    
                    if r == 1:
                        if choice1 == 1:
                            mon1 = monsters.Upgrade(pmon).hp()
                            deck.insert(0, mon1)

                        if choice1 == 2:
                            mon2 = monsters.Upgrade(pmon).hp()
                            deck.insert(1, mon2)

                        if choice1 == 3:
                            mon3 = monsters.Upgrade(pmon).hp()
                            deck.insert(2, mon3)

                    break
                except:
                    say("Wrong Input\n")

def main():
    while True:
        say("----------")
        say("1. PLAY")
        say("2. SETINGS")
        say("----------")
        say()

        x = input(":")
        say()

        if x == "1":
            game()
        

main()