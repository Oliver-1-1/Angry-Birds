import pygame
import contants
class Bird:
    def __init__(self, image_path):
        self.BirdImage = pygame.image.load(image_path)
        self.BirdRect = self.BirdImage.get_rect()
        self.BirdRect.center = (0, contants.HEIGHT - 6 * 40)
        self.IsBirdShot = False
        self.ShootIndex = 1
        self.time = 0

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
