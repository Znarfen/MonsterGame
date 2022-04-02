import random

class Normal:
    def __init__(self, at = "", xp = 1):
        self.at = at
        self.xp = xp

    def do(self):

        if self.at == "wipp":
            r = random.randint(30,70)
            return(int(r * self.xp))

        if self.at == "punch":
            r = random.randint(30,70)
            return(int(r * self.xp))

        if self.at == "cut":
            r = random.randint(45, 55)
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
            r = random.randint(40,60)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["fly"] + super().allmoves()
        return(move)

#Air moves: fly

class FireType(Normal):
    def __init__(self, at = "", xp = 1):
        super().__init__(at, xp)

    def do(self):
        if self.at == "burn":
            r = random.randint(20,80)
            return(int(r * self.xp))
        return super().do()

    def allmoves(self):
        move = ["burn"] + super().allmoves()
        return(move)

#Fire moves: burn



    



        
