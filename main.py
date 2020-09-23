import pygame
import contants
import background
import bird
import slingShot

# Init
pygame.init()
window = pygame.display.set_mode((contants.WIDTH, contants.HEIGHT), pygame.FULLSCREEN)
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


    Bird.move_bird(ParabolaList, dt)

    # Draw
    Background.draw_background(window)
    Bird.draw_bird(window)
    SlingShot.draw_parabola(window, ParabolaList)

    pygame.display.update()
