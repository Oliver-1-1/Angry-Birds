# Constants

WIDTH, HEIGHT = 1280, 846
GRAVITATION = 9.82

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def to_pygame(point):
    return int(point.x), int(-point.y + 600)

