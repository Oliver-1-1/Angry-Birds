import pygame
import pymunk

class Pig():
    def __int__(self, space, x, y):
        self.life = 20
        mass = 5
        radius = 12
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape