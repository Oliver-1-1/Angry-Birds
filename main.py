import time
import pygame
import contants
import background
import bird
import slingShot
from bird import Bird
from levels import Level
import pymunk as pm
import math
import physics
from pig import Pig
# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT))
clock = pygame.time.Clock()

# Objects
Background = background.Background("images\\background.png")
SlingShot = slingShot.SlingShot()
Physics = physics.Physics()

# Booleans
Running = True

# Other variables
ParabolaList = []

birds = []
pigs = []

space = pm.Space()
space.gravity = (0.0, -982)

physics.Polygon.create_ground(space)
def post_solve_bird_pig(arbiter, space, _):
        a, b = arbiter.shapes
        bird_body = a.body
        pig_body = b.body
        p = contants.to_pygame(bird_body.position)
        p2 = contants.to_pygame(pig_body.position)
        r = 30

        pigs_to_remove = []
        for pig in pigs:
            if pig_body == pig.body:
                pigs_to_remove.append(pig)
        for pig in pigs_to_remove:
            space.remove(pig.shape, pig.shape.body)
            pigs.remove(pig)

space.add_collision_handler(0, 2).post_solve = Physics.post_solve_bird_wood
space.add_collision_handler(0, 1).post_solve = post_solve_bird_pig

level = Level(Physics.columns, Physics.beams, space, pigs)
level.number = 0
level.load_level()

redbird = pygame.image.load("images\\red-bird3.png").convert_alpha()
pigImage = pygame.image.load("images\\rsz_pig_failed.png").convert_alpha()


while Running:
    dt = clock.tick(30)
    dt = 1.0 / 50.0 / 2.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            SlingShot.controls(event)
            if event.key == pygame.K_SPACE:
                bird = Bird(SlingShot.AngleStart, ParabolaList[0][0], ParabolaList[0][1] + 20, space,
                            SlingShot.SpeedMultiplayer)
                birds.append(bird)
    pigs_to_remove = []
    for pig in pigs:
        # print (i,pig.life)
        pig = pig.shape
        if pig.body.position.y < 0:
            pigs_to_remove.append(pig)

        p = contants.to_pygame(pig.body.position)
        x, y = p

        angle_degrees = math.degrees(pig.body.angle)
        img = pygame.transform.rotate(pigImage, angle_degrees)
        w, h = img.get_size()
        x -= w * 0.5
        y -= h * 0.5
        window.blit(img, (x, y))
    ParabolaList = SlingShot.calculate_parabola()

    # Draw
    Background.draw_background(window)

    Physics.draw_polygons(window)
    Bird.draw_bird(window, birds, redbird)

    SlingShot.draw_parabola(window, ParabolaList)
    Pig.draw_pig(window, pigs, pigImage)
    # Update
    for x in range(4):
        space.step(dt)  # two updates per frame for better stability
    pygame.display.flip()
