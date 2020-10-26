import pygame

class Cannon:
    def __init__(self):
        self.WheelImage = pygame.image.load("images\\wheel.png")
        self.WheelRect = pygame.Rect(20,20,20,20)
        self.WheelRect.center = (50, 580)

        self.BarrelImage = pygame.image.load("images\\cannon---cannon-barrel.png")
        self.BarrelRect = pygame.Rect(20,20,20,20)
        self.BarrelRect.center = (50, 575)

    def draw_cannon(self, window,surface):
        window.blit(self.WheelImage, self.WheelRect)

    def blitRotateCenter(self, window, image, topleft, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        window.blit(rotated_image, new_rect.topleft)