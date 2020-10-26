import pygame
import pymunk as pm
import contants
import math

class Pig():
    def __init__(self, x, y, space):
        # Create circle shaped body
        mass = 5
        self.radius = 14
        inertia = pm.moment_for_circle(mass, 0, self.radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y

        shape = pm.Circle(body, 14, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape


    def draw_pig(window, pigs, pigimage, pigs_to_remove, Physics):
        for pig in pigs:
            # print (i,pig.life)
            pig = pig.shape
            if pig.body.position.y < 0:
                pigs_to_remove.append(pig)

            p = contants.to_pygame(pig.body.position)
            x, y = p

            angle_degrees = math.degrees(pig.body.angle)
            img = pygame.transform.rotate(pigimage, angle_degrees)
            w, h = img.get_size()
            x -= w * 0.5
            y -= h * 0.5
            window.blit(img, (x, y))
        for column in Physics.columns:
            column.draw_poly('columns', window)
        for beam in Physics.beams:
            beam.draw_poly('beams', window)
