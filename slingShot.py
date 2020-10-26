import pygame
import math
import contants
import bird
import numpy


class SlingShot:
    def __init__(self):
        self.AngleStart = 20
        self.AngleIncrement = 5
        self.Speed = 15
        self.SpeedMultiplayer = 1

        self.YStartPos = 6

    def calculate_parabola(self):
        coord_list = []
        coord_list.clear()

        x_vel = math.cos(math.radians(self.AngleStart)) * self.Speed * self.SpeedMultiplayer
        y_vel = math.sin(math.radians(self.AngleStart)) * self.Speed * self.SpeedMultiplayer
        for x in numpy.arange(0,35.0, 0.3):
            coord_list.append((x, self.YStartPos + (y_vel / x_vel) * x - (contants.GRAVITATION * (x / x_vel) ** 2) / 2))

        return coord_list

    @staticmethod
    def draw_parabola(window, coord_list):
        for x in range(len(coord_list) - 1):
            if coord_list[x][0] <= 20:
                pygame.draw.line(window, (250, 0, 0), (coord_list[x][0] * 40, 810 - (coord_list[x][1] * 40)),
                                 (coord_list[x + 1][0] * 40, 810 - (coord_list[x + 1][1] * 40)))

    def controls(self, event):
        if event.key == pygame.K_w:
            if self.AngleStart < 85:  # clamp angle
                self.AngleStart += self.AngleIncrement

        if event.key == pygame.K_s:
            if self.AngleStart > -10:  # clamp angle
                self.AngleStart -= self.AngleIncrement

        if event.key == pygame.K_d:

            if self.SpeedMultiplayer < 5:  # clamp speed
                self.SpeedMultiplayer += 0.1

        if event.key == pygame.K_a:
            if self.SpeedMultiplayer > 0:  # clamp speed
                self.SpeedMultiplayer -= 0.1

