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
import socket
from _thread import *

import os
import sys
# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT))
clock = pygame.time.Clock()

# Objects
Background = background.Background("images\\background.png")
sling_image = pygame.image.load(
    "images\\sling-3.png").convert_alpha()
SlingShot = slingShot.SlingShot()

# Booleans
Running = True

# Other variables
ParabolaList = []

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
polys = []
beams = []
columns = []
poly_points = []
birds = []
bird_path = []
mouse_pressed = False
t1 = 0
restart_counter = False
space = pm.Space()
space.gravity = (0.0, -982)
mouse_distance = 0
rope_lenght = 90
angle = 0
x_mouse = 0
y_mouse = 0
counter = 0
game_state = 0
sling_x, sling_y = 135, 565
sling2_x, sling2_y = 160, 565
static_body = pm.Body(body_type=pm.Body.STATIC)
static_lines = [pm.Segment(static_body, (0.0, -60.0), (1200.0, -60.0), 0.0)]
static_lines1 = [pm.Segment(static_body, (1200.0, -60.0), (1200.0, 800.0), 0.0)]
for line in static_lines:
    line.elasticity = 0.95
    line.friction = 1
    line.collision_type = 3
for line in static_lines1:
    line.elasticity = 0.95
    line.friction = 1
    line.collision_type = 3
space.add(static_lines)
wall = False
def post_solve_bird_wood(arbiter, space, _):
    """Collision between bird and wood"""
    poly_to_remove = []
    if arbiter.total_impulse.length > 1100:
        a, b = arbiter.shapes
        for column in columns:
            if b == column.shape:
                poly_to_remove.append(column)
        for beam in beams:
            if b == beam.shape:
                poly_to_remove.append(beam)
        for poly in poly_to_remove:
            if poly in columns:
                columns.remove(poly)
            if poly in beams:
                beams.remove(poly)
        space.remove(b, b.body)


space.add_collision_handler(0, 2).post_solve=post_solve_bird_wood
level = Level(columns, beams, space)
level.number = 0
level.load_level()

def to_pygame(p):
    """Convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)

redbird = pygame.image.load(
    "images\\red-bird3.png").convert_alpha()

while Running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            SlingShot.controls(event)
            if event.key == pygame.K_SPACE:
                bird = Bird(mouse_distance, SlingShot.AngleStart, ParabolaList[0][0], ParabolaList[0][1] + 20, space, SlingShot.SpeedMultiplayer)
                birds.append(bird)

            if event.key == pygame.K_w:
            # Toggle wall
                if wall:
                    space.remove(static_lines1)
                    wall = False
                else:
                    space.add(static_lines1)
                    wall = True

            # Release new bird
            if level.number_of_birds > 0:
                level.number_of_birds -= 1
                t1 = time.time() * 1000
                xo = 150
                yo = 41

    Background.draw_background(window)
    rect = pygame.Rect(50, 0, 70, 220)
    window.blit(sling_image, (138, 535), rect)
    # if bird is shot, disable controls for the parabola
    ParabolaList = SlingShot.calculate_parabola()

    counter += 1

    for column in columns:
        column.draw_poly('columns', window)
    for beam in beams:
        beam.draw_poly('beams', window)
        # Update physics
    dt = 1.0 / 50.0 / 2.
    for x in range(2):
        space.step(dt)  # make two updates per frame for better stability

    for bird in birds:

        p = to_pygame(bird.shape.body.position)
        x, y = p
        x -= 22
        y -= 20
        window.blit(redbird, (x, y))

    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(window, (150, 150, 150), False, [p1, p2])
    SlingShot.draw_parabola(window, ParabolaList)
    for x in range(2):
        space.step(dt)
    rect = pygame.Rect(0, 0, 60, 200)
    window.blit(sling_image, (120, 535), rect)
    pygame.display.flip()
    pygame.display.update()
