import random

class Attack:
    def __init__(self, at, xp = 1):
        self.at = at
        self.xp = xp

    def do(self):

        if self.at == "wipp":
            r = random.randint(30,70)
            return(int(r * self.xp))

        if self.at == "punch":
            r = random.randint(30,70)
            return(int(r * self.xp))

#Normal moves: wip, punch

class AirType(Attack):
    def __init__(self, at=0, xp=1):
        super().__init__(at, xp)

    def do(self):
        if self.at == "fly":
            r = random.randint(40,60)
            return(int(r * self.xp))
        return super().do()

#Air moves: fly

class FireType(Attack):
    def __init__(self, at=0, xp=1):
        super().__init__(at, xp)

    def do(self):
        if self.at == "burn":
            r = random.randint(20,80)
            return(int(r * self.xp))
        return super().do()

#Fire moves: burn



    



        
