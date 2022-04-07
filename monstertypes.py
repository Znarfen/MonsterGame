import random

class Normal:
    def __init__(self, at = "", xp = 1):
        self.at = at
        self.xp = xp

    def do(self):

        if self.at == "wipp":
            r = random.randint(10, 30)
            return(int(r * self.xp))

        if self.at == "punch":
            r = random.randint(5, 15)
            return(int(r * self.xp))

        if self.at == "cut":
            r = random.randint(1, 10)
            return(int(r * self.xp))

    def allmoves(self):
        move = ["wipp", "punch", "cut"]
        return(move)

#Normal moves: wip, punch, cut

class AirType(Normal):
    def __init__(self, at = "", xp = 1):
        super().__init__(at, xp)

    def do(self):

        if self.at == "fly":
            r = random.randint(20, 25)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["fly"] + super().allmoves()
        return(move)

#Air moves: fly

class GhostType(AirType):
    def __init__(self, at="", xp=1):
        super().__init__(at, xp)

    def do(self):

        if self.at == "Death Ray":
            r = random.randint(25, 30)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["Death Ray"] + super().allmoves()
        return(move)

# Ghost moves: Death Ray

class FireType(Normal):
    def __init__(self, at = "", xp = 1):
        super().__init__(at, xp)

    def do(self):

        if self.at == "burn":
            r = random.randint(15, 30)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["burn"] + super().allmoves()
        return(move)

#Fire moves: burn

class WaterType(Normal):
    def __init__(self, at="", xp=1):
        super().__init__(at, xp)

    def do(self):

        if self.at == "splach":
            r = random.randint(10, 35)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["splach"] + super().allmoves()
        return(move)
    
class ElementalType(WaterType, FireType):
    def __init__(self, at="", xp=1):
        super().__init__(at, xp)

    def do(self):

        if self.at == "Obsidian Throw":
            r = random.randint(10, 35)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["Obsidian Throw"] + super().allmoves()
        return(move)





    



        
