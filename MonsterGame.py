import monsters


level = 0

mon1 = monsters.Generator().new()
mon2 = monsters.Generator().new()
mon3 = monsters.Generator().new()

def about(mon):
    n1 = ("name = " + mon.name())
    n2 = ("power = " + str(mon.power()))
    n3 = ("hp = " + str(mon.hp()))
    n4 = ("type = " + mon.type())
    print(n1, "/", n2, "/", n3, "/", n4)
    print()

deck = [mon1, mon2, mon3]

while True:
    level += 1

    ii = 1
    print("This is the deck you have:")
    for i in deck:
        print("Monster-" + str(ii) + ":")
        about(i)
        ii += 1
    print("")

    opponent = monsters.Generator().new()
    print("About your opponent:")
    about(opponent)

    choice = int(input(":"))
    

    