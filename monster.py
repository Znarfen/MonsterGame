import moveset

ph = 10
oh = 10
while ph > 0 and oh > 0:

    print("player health:", ph, "\noponent health:", oh, " \n\n")
    at = int(input(" 1, Punch \n 2, Wip \n\n:"))

    if at == 1:
        at = "Punch"
    if at == 2:
        at = "Wip"

    at = moveset.Do(at).attack()
    print(at)
    oh = oh - at

    print("\n\nÄggis use Punch\n\n")

    x = moveset.Do("Punch").attack()
    ph = ph - x







