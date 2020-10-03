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

import os
import sys
# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT), pygame.FULLSCREEN)
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
space.gravity = (0.0, -700.0)
mouse_distance = 0
rope_lenght = 90
angle = 0
x_mouse = 0
y_mouse = 0
counter = 0
game_state = 0
sling_x, sling_y = 135, 450
sling2_x, sling2_y = 160, 450
static_body = pm.Body(body_type=pm.Body.STATIC)
static_lines = [pm.Segment(static_body, (0.0, -60.0), (1200.0, -060.0), 0.0)]
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

space.add_collision_handler(0, 2).post_solve=post_solve_bird_wood
level = Level(columns, beams, space)
level.number = 0
level.load_level()


def vector(p0, p1):
    """Return the vector of the points
    p0 = (xo,yo), p1 = (x1,y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """Return the unit vector of the points
    v = (a,b)"""
    h = ((v[0]**2)+(v[1]**2))**0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)


def distance(xo, yo, x, y):
    """distance between points"""
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d

def restart():
    """Delete all objects of the level"""
    pigs_to_remove = []
    birds_to_remove = []
    columns_to_remove = []
    beams_to_remove = []

    for bird in birds:
        birds_to_remove.append(bird)
    for bird in birds_to_remove:
        space.remove(bird.shape, bird.shape.body)
        birds.remove(bird)
    for column in columns:
        columns_to_remove.append(column)
    for column in columns_to_remove:
        space.remove(column.shape, column.shape.body)
        columns.remove(column)
    for beam in beams:
        beams_to_remove.append(beam)
    for beam in beams_to_remove:
        space.remove(beam.shape, beam.shape.body)
        beams.remove(beam)

def to_pygame(p):
    """Convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)

redbird = pygame.image.load(
    "images\\red-bird3.png").convert_alpha()

def sling_action():
    """Set up sling behavior"""
    global mouse_distance
    global rope_lenght
    global angle
    global x_mouse
    global y_mouse
    # Fixing bird to the sling rope
    v = vector((sling_x, sling_y), (x_mouse, y_mouse))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(sling_x, sling_y, x_mouse, y_mouse)
    pu = (uv1*rope_lenght+sling_x, uv2*rope_lenght+sling_y)
    bigger_rope = 102
    x_redbird = x_mouse - 20
    y_redbird = y_mouse - 20
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 20
        puy -= 20
        pul = pux, puy
        window.blit(redbird, pul)
        pu2 = (uv1*bigger_rope+sling_x, uv2*bigger_rope+sling_y)
        pygame.draw.line(window, (0, 0, 0), (sling2_x, sling2_y), pu2, 5)
        window.blit(redbird, pul)
        pygame.draw.line(window, (0, 0, 0), (sling_x, sling_y), pu2, 5)
    else:
        mouse_distance += 10
        pu3 = (uv1*mouse_distance+sling_x, uv2*mouse_distance+sling_y)
        pygame.draw.line(window, (0, 0, 0), (sling2_x, sling2_y), pu3, 5)
        window.blit(redbird, (x_redbird, y_redbird))
        pygame.draw.line(window, (0, 0, 0), (sling_x, sling_y), pu3, 5)
    # Angle of impulse
    dy = y_mouse - sling_y
    dx = x_mouse - sling_x
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy))/dx)


while Running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            SlingShot.controls(event)
            if event.key == pygame.K_w:
            # Toggle wall
                if wall:
                    space.remove(static_lines1)
                    wall = False
                else:
                    space.add(static_lines1)
                    wall = True
        if (pygame.mouse.get_pressed()[0] and x_mouse > 100 and
                x_mouse < 250 and y_mouse > 370 and y_mouse < 550):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and
                event.button == 1 and mouse_pressed):
            # Release new bird
            mouse_pressed = False
            if level.number_of_birds > 0:
                level.number_of_birds -= 1
                t1 = time.time() * 1000
                xo = 154
                yo = 156
                if mouse_distance > rope_lenght:
                    mouse_distance = rope_lenght
                if x_mouse < sling_x + 5:
                    bird = Bird(mouse_distance, angle, xo, yo, space)
                    birds.append(bird)
                else:
                    bird = Bird(-mouse_distance, angle, xo, yo, space)
                    birds.append(bird)



    x_mouse, y_mouse = pygame.mouse.get_pos()
    Background.draw_background(window)
    rect = pygame.Rect(50, 0, 70, 220)
    window.blit(sling_image, (138, 420), rect)
    # if bird is shot, disable controls for the parabola
    ParabolaList = SlingShot.calculate_parabola()
    if mouse_pressed and level.number_of_birds > 0:
        sling_action()
    else:
        if  time.time() * 1000 - t1 > 300 and level.number_of_birds > 0:
            window.blit(redbird, (130, 426))
        else:
            pygame.draw.line(window, (0, 0, 0), (sling_x, sling_y - 8),
                             (sling2_x, sling2_y - 7), 5)
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

        if counter >= 3 and time.time() - t1 < 5:
            bird_path.append(p)
            restart_counter = True
    if restart_counter:
        counter = 0
        restart_counter = False
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
    window.blit(sling_image, (120, 420), rect)
    pygame.display.flip()
    pygame.display.update()
