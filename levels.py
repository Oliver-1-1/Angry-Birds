from physics import Polygon
from pig import Pig

class Level:
    def __init__(self, columns, beams, space, pigs):
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4

        self.bool_space = False

    def build_0(self):
        pig1 = Pig(980, 100, self.space)
        pig2 = Pig(980, 182, self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)
        p = (950, -50)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, -50)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 20)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 70)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 70)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 110)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def load_level(self):
        try:
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()
