import pymunk as pm
from pymunk import Vec2d
import pygame
import math
import contants


class Physics:
    def __init__(self):
        self.columns = []
        self.beams = []
        self.pigs = []

    def post_solve_bird_wood(self, arbiter, space, _):
        poly_to_remove = []
        if arbiter.total_impulse.length > 1100:
            a, b = arbiter.shapes
            for column in self.columns:
                if b == column.shape:
                    poly_to_remove.append(column)
            for beam in self.beams:
                if b == beam.shape:
                    poly_to_remove.append(beam)
            for poly in poly_to_remove:
                if poly in self.columns:
                    self.columns.remove(poly)
                if poly in self.beams:
                    self.beams.remove(poly)
            space.remove(b, b.body)



    def draw_polygons(self, window):
        for column in self.columns:
            column.draw_poly('columns', window)
        for beam in self.beams:
            beam.draw_poly('beams', window)


class Polygon:
    def __init__(self, pos, length, height, space):
        self.body = pm.Body(5, 1000)
        self.body.position = pos

        self.shape = pm.Poly.create_box(self.body, (length, height))
        self.shape.friction = 0.5
        self.shape.collision_type = 2
        space.add(self.body, self.shape)

        wood = pygame.image.load("images\\wood.png").convert_alpha()
        self.beam_image = wood.subsurface(pygame.Rect(251, 357, 86, 22)).copy()

        wood2 = pygame.image.load("images\\wood2.png").convert_alpha()
        self.column_image = wood2.subsurface(pygame.Rect(16, 252, 22, 84)).copy()

    def draw_poly(self, element, window):
        poly = self.shape
        ps = poly.get_vertices()
        ps.append(ps[0])
        ps = map(contants.to_pygame, ps)
        ps = list(ps)

        if element == 'beams':
            p = poly.body.position
            p = Vec2d(contants.to_pygame(p))
            rotated_logo_img = pygame.transform.rotate(self.beam_image, math.degrees(poly.body.angle) + 180)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p -= offset
            window.blit(rotated_logo_img, (p.x, p.y))

        if element == 'columns':
            p = poly.body.position
            p = Vec2d(contants.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            window.blit(rotated_logo_img, (np.x, np.y))

    @staticmethod
    def create_ground(space):
        static_body = pm.Body(body_type=pm.Body.STATIC)

        # Create ground
        static_lines = [pm.Segment(static_body, (0.0, -60.0), (1200.0, -60.0), 0.0)]
        for i in static_lines:
            i.elasticity = 0.95
            i.friction = 1
            i.collision_type = 3

        static_lines1 = [pm.Segment(static_body, (1200.0, -60.0), (1200.0, 800.0), 0.0)]
        for b in static_lines1:
            b.elasticity = 0.95
            b.friction = 1
            b.collision_type = 3

        space.add(static_lines)
