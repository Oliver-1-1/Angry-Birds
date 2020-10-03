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
        self.SpeedIncrement = 1

        self.Player1Up = pygame.K_w
        self.Player1Down = pygame.K_s

        self.Player2Up = pygame.K_UP
        self.Player2Down = pygame.K_DOWN
        self.YStartPos = 6

    def calculate_parabola(self):
        coord_list = []
        coord_list.clear()

        x_vel = math.cos(math.radians(self.AngleStart)) * self.Speed
        y_vel = math.sin(math.radians(self.AngleStart)) * self.Speed

        for x in numpy.arange(0, 35.0, 0.3):
            coord_list.append((x, self.YStartPos + (y_vel / x_vel) * x - (contants.GRAVITATION * (x / x_vel) ** 2) / 2))

        return coord_list

    @staticmethod
    def draw_parabola(window, coord_list):
        for x in range(len(coord_list) - 1):
            if coord_list[x][0] <= 20:
                pygame.draw.line(window, (250, 0, 0), (coord_list[x][0] * 40, 719 - (coord_list[x][1] * 40)),
                                 (coord_list[x + 1][0] * 40, 719 - (coord_list[x + 1][1] * 40)))

    def controls(self, event):
        if event.key == pygame.K_w:
            if self.AngleStart < 85:  # clamp angle
                self.AngleStart += self.AngleIncrement

        if event.key == pygame.K_s:
            if self.AngleStart > -10:  # clamp angle
                self.AngleStart -= self.AngleIncrement

        if event.key == pygame.K_d:

            if self.Speed < 20:  # clamp speed
                self.Speed += self.SpeedIncrement

        if event.key == pygame.K_a:
            if self.Speed > 1:  # clamp speed
                self.Speed -= self.SpeedIncrement

