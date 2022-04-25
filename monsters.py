

class NoType():
    def __init__(self, at = 0, health = 0, monstername = "", monstertype = ""):
        self.at = at
        self.health = health
        self.monstername = monstername
        self.monstertype = monstertype

    def attack(self):
        return(self.at)

    def name(self):
        return(self.monstername)

    def hp(self):
        return(self.health)

    def type(self):
        return(self.monstertype)

class Fire(NoType):
    def __init__(self, at = 0, health = 0, monstername = "", monstertype = "Fire"):
        super().__init__(at, health, monstername, monstertype)

class Water(NoType):
    def __init__(self, at = 0, health = 0, monstername = "", monstertype = "Water"):
        super().__init__(at, health, monstername, monstertype)

class Grass(NoType):
    def __init__(self, at = 0, health = 0, monstername = "", monstertype = "Grass"):
        super().__init__(at, health, monstername, monstertype)



class Battle():
    def __init__(self, mon1, mon2):
        self.mon1 = mon1
        self.mon2 = mon2

    def attack(self):
        if self.mon1.type() == self.mon2.type():
            return(self.mon1.attack())

        if self.mon1.type() == "Fire":
            if self.mon2.type() == "Grass":
                return(self.mon1.attack() + 2)
            if self.mon2.type() == "Water":
                return(self.mon1.attack() - 2)

        if self.mon1.type() == "Water":
            if self.mon2.type() == "Grass":
                return(self.mon1.attack() - 2)
            if self.mon2.type() == "Fire":
                return(self.mon1.attack() + 2)

        if self.mon1.type() == "Grass":
            if self.mon2.type() == "Water":
                return(self.mon1.attack() + 2)
            if self.mon2.type() == "Fire":
                return(self.mon1.attack() - 2)

class uppgrade():
    def __init__(self, mon):
        self.mon = mon

    def hp(self):
        at = self.mon.attack()
        health = self.mon.hp() + 2
        name = self.mon.name()
        type = self.mon.type()

        return(NoType(at, health, name, type))

    def attack(self):
        at = self.mon.attack() + 2
        health = self.mon.hp()
        name = self.mon.name()
        type = self.mon.type()

        return(NoType(at, health, name, type))

FlygFan = Fire(3, 1, "FlygFan")

Äggis = Grass(1, 4, "Äggis")

SlemHög = Water(2, 2, "SlemHög")

Makaias = Water(1, 5, "Makaias")

print(Battle(Makaias, Äggis).attack())


