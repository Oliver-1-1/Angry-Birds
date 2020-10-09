import pygame
import contants
import pymunk as pm
from pymunk import Vec2d
import math
import slingShot
class Bird:
    def __init__(self, distance, angle, x, y, space, slingShotSpeed):
        self.life = 20
        mass = 5
        radius = 12
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        power = 100 * 47.5 * slingShotSpeed
        impulse = power * Vec2d(1, 0)
        angle = -angle
        body.apply_impulse_at_local_point(impulse.rotated(math.radians(-angle)))
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def draw_bird(self, window):
        window.blit(self.BirdImage, self.BirdRect)

    def move_bird(self, cords, dt):
        if dt > 0.005:
            if self.IsBirdShot:
                self.BirdRect.center = (cords[self.ShootIndex][0] * 40, 719 - (cords[self.ShootIndex][1] * 40))
                self.ShootIndex += 1

                # Respawn bird
                if self.BirdRect.centery > contants.HEIGHT or self.BirdRect.centerx > contants.WIDTH:
                    self.BirdRect.center = (0, contants.HEIGHT - 6 * 40)
                    print("hi")
                    self.IsBirdShot = False
                    self.ShootIndex = 0
        self.time = 0
