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
import cannon

# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT))
clock = pygame.time.Clock()

Background = background.Background("images\\background.png")
SlingShot = slingShot.SlingShot()
Physics = physics.Physics()
Cannon = cannon.Cannon()

Running = True

ParabolaList = []

birds = []
pigs = []
redbird = pygame.image.load("images\\red-bird3.png").convert_alpha()
pigImage = pygame.image.load("images\\rsz_pig_failed.png").convert_alpha()


space = pm.Space()
space.gravity = (0.0, -982)

physics.Polygon.create_ground(space)


def post_solve_bird_pig(arbiter, space, _):
    if arbiter.total_impulse.length > 1500:

        a, b = arbiter.shapes
        bird_body = a.body
        pig_body = b.body

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

    # Calculates the coordinated the parabola should be drawn at
    ParabolaList = SlingShot.calculate_parabola()

    # Draw
    Background.draw_background(window)
    Cannon.blitRotateCenter(window, Cannon.BarrelImage, Cannon.BarrelRect.topleft, SlingShot.AngleStart)
    Cannon.draw_cannon(window, window)
    Physics.draw_polygons(window)
    Bird.draw_bird(window, birds, redbird)
    Pig.draw_pig(window, pigs, pigImage, pigs_to_remove, Physics)
    SlingShot.draw_parabola(window, ParabolaList)
    # Update
    for x in range(4):
        space.step(dt)
    pygame.display.flip()
