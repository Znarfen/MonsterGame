import monsters
import random
import time

# Printar texten i segment
def say(a = "", b = "", c = "", d = ""):
    print(a, b, c, d)
    time.sleep(0.2)

# Se vad monstrets stats är
def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    say(n1 + " / " + n2 + " / " + n3 + " / " + n4)
    say()

# Visar ens deck
def showdeck(deck):
    say("This is the deck you have:")
    ii = 1
    for i in deck:
        say(str(ii) + ". " + " Monster-" + str(ii) + ":")
        about(i)
        ii += 1
    say("")

# Se (r) och kunna ändra (a) på score.txt
def score(do = "r", sc = 0):

    # Tar info
    f = open("score.txt", "r")
    rinfo = f.read().split("\n")

    # Sorterar info
    sinfo = []
    for x in rinfo:
        s = x.split(" ")
        s1 = int(s[0])
        s2 = str(s[1])
        sinfo.append([s1, s2])

    tt = 0
    for y in sinfo:
        t = y[0]
        if t > tt:
            tt = t

    f.close()
    say("----------")

    # Lägger till ett score
    if do == "w":
        f = open("score.txt", "a")

        while True:
            name = str(input("Enter a five leter name: "))
            say()

            ex = False
            for yy in sinfo:
                if yy[1] == name:
                    name = "abcdef"
                    say("That name alredy exist!")
                    ex = True

            if len(name) == 5:
                say()
                break

            if ex == False:
                say("Wrong Input")
                say()

        f.write("\n" + str(sc) + " " + name)
        f.close()

        say("Your score is now stored!")
        f.close()

    # Läser av Score.txt
    if do == "r":
        f = open("score.txt", "r")

        say("SCOREBOARD:")
        say("----------")
        k = 0
        for z in range(tt + 1, 0, -1):
            for zz in sinfo:
                if z == zz[0]:
                    k += 1
                    if k > 9:
                        break
                    say(str(k) + ": ", zz[1], zz[0])
        say("----------")
        f.close()

# Själva spelet
def game():

    # Föbereder ens deck
    mon1 = monsters.Generator(2, "Fire").new()
    mon2 = monsters.Generator(2, "Water").new()
    mon3 = monsters.Generator(2, "Grass").new()
    level = 0
    deck = [mon1, mon2, mon3]

    # Startar spelet
    while True:
        
        level += 1
        say("----------------")
        say()
        
        showdeck(deck)

        # Skapar mostondare
        opponent = monsters.Generator(level * level).new()
        say("About your opponent:")
        about(opponent)

        # Väljer sitt monster
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

        # Monster börjar sloss
        while True:
            pa = monsters.Battle(pmon, opponent).attack()
            oa = monsters.Battle(opponent, pmon).attack()

            # Utan bonus (monstrets typ)
            rpa = pmon.power()
            roa = opponent.power()

            h += 1
            say("Round " + str(h))
            say()

            pb = pa - rpa
            ob = oa - roa

            # Lägger till plussteken
            if pb >= 0:
                pb = "+" + str(pb)
            if ob >= 0:
                ob = "+" + str(ob)

            # Vissar hur det går för man
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

            # Vem som vinner / fölorar
            if (0 >= oh) or (0 >= ph):

                if ph <= oh:
                    win = False
                    say(pmon.name() + " faild")
                    break

                if oh < ph:
                    win = True
                    say(opponent.name() + " faild")
                    break

            say()
            input("Press ENTER ")
            say()
            say("------------")
            say()

        say()
        say("Score:", level)
        say()

        # Om man vinner
        if win == True:
            say("You won!")
            input("Press ENTER ")
            say()

        # Dödar ett monster
        if win == False:
            say("The opponent won!")
            input("Press ENTER ")
            say()
            say("Your monster", pmon.name(), "is now ded!")
            say()
            deck.remove(deck[choice-1])

            # Avslut på spelet
            if len(deck) == 0:
                say("All your monsters has ben defeted!")
                say()
                input("Press ENTER ")
                say()

                score("w", level)
                break

        say()
        ii = 1

        # Om man vinner mot en monståndare
        if win == True:
            showdeck(deck)

            # Uppgradera ett monster
            while True:
                try:
                    s = "Witch monster do you want to upgrade? :"
                    choice1 = int(input(s))
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

# Huvudmenyn
def main():
    while True:
        score()
        say("1. PLAY")
        say("----------")
        say()

        x = input(":")
        say()

        if x == "1":
            game()
        
main()