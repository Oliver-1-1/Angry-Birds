from physics import Polygon


class Level():
    def __init__(self, columns, beams, space):

        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space = False

    def open_flat(self, x, y, n):
        """Create a open flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+50)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.columns.append(Polygon(p, 20, 85, self.space))

    def build_0(self):
        """level 0"""
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
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000

    def load_level(self):
        try:
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()