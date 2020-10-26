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
        pig1 = Pig(960, 110, self.space)
        pig2 = Pig(960, 192, self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)

        self.beams.append(Polygon((960, 110), 85, 20, self.space))
        self.beams.append(Polygon((960, 20), 85, 20, self.space))

        self.columns.append(Polygon((930, -50), 20, 85, self.space))
        self.columns.append(Polygon((990, -50), 20, 85, self.space))
        self.columns.append(Polygon((930, 70), 20, 85, self.space))
        self.columns.append(Polygon((990, 70), 20, 85, self.space))

        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def load_level(self):
        build_name = "build_" + str(self.number)
        getattr(self, build_name)()

