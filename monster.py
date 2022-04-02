import moveset
import random

ph = 1000
oh = 1000

mo = moveset.AirType().allmoves()
x = random.choice(mo)
mo.remove(x)
y =random.choice(mo)

mo = ["burn", "punch"]

while True:
    if oh < 0:
        print("Player won")
        break
    if ph < 0:
        print("Oponent won")
        break

    print("player:", ph)
    print("oponent", oh)
    print()

    z = input("1)" + x + "\n2)" + y +"\n \n:")
    if z == "1":
        z = x
    if z == "2":
        z = y

    at = moveset.AirType(z).do()
    oh = oh - at
    print("Player:", z)
    print(at, "was made by the player\n")

    r = random.choice(mo)
    
    at = moveset.FireType(r).do()
    ph = ph - at

    print("Oponent:", r,)
    print(at, "was made by the oponent\n")










