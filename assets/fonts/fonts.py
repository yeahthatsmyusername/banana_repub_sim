import pygame

class Fonts:
    def __init__(self):
        self.pygame = pygame
        self.all_fonts = {}
        self.all_fonts["main"] = self.pygame.font.Font("assets/fonts/DisposableDroidBB.ttf", 86)

    def getFont(self, font_name):
        return self.all_fonts[font_name]