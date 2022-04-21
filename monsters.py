from mimetypes import init
import monstertypes


class Rat():
    def __init__(self, at = 1, hp = 1):
        self.at = at
        self.hp = hp

    def attack(self):
        return(self.at)

class FlygFan(Rat):
    def __init__(self, at=3, hp=1):
        super().__init__(at, hp)


print(FlygFan().attack())