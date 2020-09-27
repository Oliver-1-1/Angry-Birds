import pygame
import contants
import background
import bird
import slingShot
import pymunk
from pymunk import pygame_util
import random
# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT))
clock = pygame.time.Clock()

# Objects
Background = background.Background("images\\background2.jpg")
Bird = bird.Bird("images\\red-bird3.png")
SlingShot = slingShot.SlingShot()

# Booleans
Running = True

# Other variables
ParabolaList = []
time = 0

def add_ball(space):
    """Add a ball to the given space at a random position"""
    space.gravity = (0, -900.0)
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(120,380)
    body.position = x, 550
    shape = pymunk.Circle(body, radius, (0,0))
    space.add(body, shape)
    return shape
def zero(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0,0), damping, dt)

def add_L(space):
    space.gravity = (0,0)

    body = pymunk.Body(10, 10000)
    body.position = (300, 50)
    body.velocity_func = zero
    
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)


    space.add(l1, l2, body)
    return l1,l2

space = pymunk.Space()

lines = add_L(space)
balls = []
draw_options = pymunk.pygame_util.DrawOptions(window)

ticks_to_next_ball = 10
while Running:
    dt = clock.tick(30)
    Bird.time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            SlingShot.controls(event, Bird)

    # if bird is shot, disable controls for the parabola
    if not Bird.IsBirdShot:
        ParabolaList = SlingShot.calculate_parabola()
    ticks_to_next_ball -= 1
    if ticks_to_next_ball <= 0:
        ticks_to_next_ball = 25
        ball_shape = add_ball(space)
        balls.append(ball_shape)

    window.fill((255, 255, 255))

    balls_to_remove = []
    for ball in balls:
        if ball.body.position.y < 50:
            balls_to_remove.append(ball)

    for ball in balls_to_remove:
        space.remove(ball, ball.body)
        balls.remove(ball)


    space.step(1 / 50.0)

    Bird.move_bird(ParabolaList, dt)

    # Draw
    Background.draw_background(window)
    Bird.draw_bird(window)
    SlingShot.draw_parabola(window, ParabolaList)
    space.debug_draw(draw_options)


    pygame.display.update()
