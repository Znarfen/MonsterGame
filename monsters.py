import requests
import random

class NoType():
    def __init__(self, at = 0, health = 0, monstername = "", monstertype = ""):
        self.at = at
        self.health = health
        self.monstername = monstername
        self.monstertype = monstertype

    def power(self):
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
            ret = (self.mon1.power())

        if self.mon1.type() == "Fire":
            if self.mon2.type() == "Grass":
                ret = (self.mon1.power() + 2)
            if self.mon2.type() == "Water":
                return(self.mon1.power() - 2)

        if self.mon1.type() == "Water":
            if self.mon2.type() == "Grass":
                ret = (self.mon1.power() - 2)
            if self.mon2.type() == "Fire":
                ret = (self.mon1.power() + 2)

        if self.mon1.type() == "Grass":
            if self.mon2.type() == "Water":
                ret = (self.mon1.power() + 2)
            if self.mon2.type() == "Fire":
                ret = (self.mon1.power() - 2)

        if ret < 0:
            ret = 0
        return(ret)

class Upgrade():
    def __init__(self, mon):
        self.mon = mon

    def hp(self):
        at = self.mon.power()
        health = self.mon.hp() + 2
        name = self.mon.name()
        type = self.mon.type()

        return(NoType(at, health, name, type))

    def at(self):
        at = self.mon.power() + 2
        health = self.mon.hp()
        name = self.mon.name()
        type = self.mon.type()

        return(NoType(at, health, name, type))

class Generator():
    def __init__(self, level = 1, type = ""):
        self.level = level
        self.type = type

    def new(self):
        names = []
        listname = ["Ägg", "Jon", "Matt", "Nick, Fregroj", "Nick", "Zac", 
        "No", "Red", "Blue", "Yelow", "Grean", "Demo", "Null", "Gass", 
        "One", "PeePee", "UwU", "No", "Mon", "OwO", "Lul", "Fast", "Bot"]

        try:
            name1 = requests.get("https://random-word-api.herokuapp.com/word").json()[0]
            name2 = random.choice(listname)
            
        except:

            name1 = random.choice(listname)
            name2 = random.choice(listname)

        names.append(name1 + "-" + name2)
        names.append(name2 + "-" + name1)

        g = self.level + 10
        num = random.randint(1, g)
        at = num
        hp = g - num
        name = (random.choices(names)[0].upper())

        if self.type == "":
            r = random.choice(["Fire", "Water", "Grass"])
        else:
            r = self.type

        if r == "Fire":
            return(Fire(at, hp, name))

        if r == "Water":
            return(Water(at, hp, name))

        if r == "Grass":
            return(Grass(at, hp, name))


#new = Generator().new()
#print(new.name(), new.power(), new.hp(), new.type())





