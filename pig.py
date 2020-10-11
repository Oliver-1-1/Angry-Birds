import pygame
import pymunk as pm
import contants


class Pig():
    def __init__(self, x, y, space):
        # Create circle shaped body
        body = pm.Body(5, pm.moment_for_circle(5, 0, 14, (0, 0)))
        body.position = x, y
        shape = pm.Circle(body, 14, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape

    @staticmethod
    def draw_pig(window, pig_list, pig_image):
        for pig in pig_list:
            x, y = contants.to_pygame(pig.shape.body.position)
            window.blit(pig_image, (x, y))
