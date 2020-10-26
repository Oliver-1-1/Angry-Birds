import pygame
import contants
import pymunk as pm
from pymunk import Vec2d
import math
import slingShot
import contants


class Bird:
    def __init__(self, angle, x, y, space, sling_shot_speed):

        # Create circle shaped body
        body = pm.Body(5, pm.moment_for_circle(5, 0, 12, (0, 0)))
        body.position = x, y
        shape = pm.Circle(body, 12, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)

        # Apply an impulse so it moves
        impulse = 100 * 47.5 * sling_shot_speed * Vec2d(1, 0)
        body.apply_impulse_at_local_point(impulse.rotated(math.radians(angle)))

        self.body = body
        self.shape = shape

    @staticmethod
    def draw_bird(window, birds_list, bird_image):
        for bird in birds_list:
            x, y = contants.to_pygame(bird.shape.body.position)
            x -= 22
            y -= 22
            window.blit(bird_image, (x, y))

