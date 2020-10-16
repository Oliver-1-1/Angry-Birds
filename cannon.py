import pygame

class Cannon:
    def __init__(self):
        self.WheelImage = pygame.image.load("images\\wheel.png")
        self.WheelRect = pygame.Rect(20,20,20,20)
        self.WheelRect.center = (50, 580)

        self.BarrelImage = pygame.image.load("images\\cannon---cannon-barrel.png")
        self.BarrelRect = pygame.Rect(20,20,20,20)
        self.BarrelRect.center = (50, 580)

        self.offset = pygame.math.Vector2(50,0)
        self.angle = 0
        self.pivot = self.WheelRect.center
    def draw_cannon(self, window,surface):
        pygame.draw.polygon(surface, pygame.Color('dodgerblue3'), ((0, 0), (140, 30), (0, 60)))

        window.blit(self.rotated_image, self.rect)
        window.blit(self.WheelImage, self.WheelRect)


    def rotate(self, surface, angle, pivot, offset):
        rotaded_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotaded_offset = offset.rotate(angle)

        rect = rotaded_image.get_rect(center=pivot+rotaded_offset)
        return rotaded_image, rect



    def rotate_barrel(self, surface):
        self.rotated_image, self.rect = self.rotate(surface, self.angle, self.pivot, self.offset)
        self.angle += 20
