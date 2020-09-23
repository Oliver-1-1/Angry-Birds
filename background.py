import pygame

class Background:
    def __init__(self, image_path):
        self.background_image = pygame.image.load(image_path).convert()
        self.background_rect = self.background_image.get_rect()

    def draw_background(self, window):
        window.blit(self.background_image, self.background_rect)
