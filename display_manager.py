import os
import pygame
from assets.fonts.fonts import Fonts

class  Display_manager:

    SIZE = None
    SCREEN_X = 0
    SCREEN_Y = 30
    WHITE = (255, 255, 245)

    def __init__(self, pygame):
        self.pygame = pygame
        infoObject = self.pygame.display.Info()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Display_manager.SCREEN_X, Display_manager.SCREEN_Y)
        Display_manager.SIZE = (infoObject.current_w, infoObject.current_h)
        self.display = self.pygame.display.set_mode(Display_manager.SIZE)
        self.background_color = Display_manager.WHITE

    def registerSpriteManager(self, sm):
        self.sprite_manager = sm

    def registerMenuManager(self, mm):
        self.menu_manager = mm

    def setBackground(self, color):
        self.background_color = color

    def updateBackground(self):
        self.display.fill(self.background_color)

    def renderSprites(self):
        all_sprites = self.sprite_manager.getSprites()
        for sprite in all_sprites:
            self.display.blit(sprite.image, sprite.getPosition())

    def renderMenu(self):
        menu_sprites = self.menu_manager.getActiveMenuSprites()
        for menu_sprite in menu_sprites:
            self.display.blit(menu_sprite.image, menu_sprite.getPosition())
            #print(menu_sprite.image.get_size())

    def update(self):
        self.updateBackground()
        if self.menu_manager.menu_is_active:
            self.renderMenu()
        else:
            self.renderSprites()
        font = pygame.font.Font("assets/fonts/DisposableDroidBB.ttf", 86)
        rendered_text = font.render('hello', True, (0, 0, 0))
        self.display.blit(rendered_text, (0, 0))
        self.pygame.display.update()