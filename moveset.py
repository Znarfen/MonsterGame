

class Attack:
    def __init__(self, at = 0, xp = 1):
        self.at = at
        self.xp = xp

    def normal(self):

        if self.at == 0:
            return(0 * self.xp)

        if self.at == 1:
            return(float(1 * self.xp))

        if self.at == 2:
            return(float(3 * self.xp))

    
class Fly(Attack):
    def __init__(self, at=0, xp=1):
        super().__init__(at, xp)



#class Ground(Attack):


        
