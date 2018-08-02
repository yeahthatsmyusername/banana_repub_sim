from display_manager import Display_manager
from sprite_manager import Sprite_manager
from sprite import Sprite
from menu_man import Menu_manager

class Game_manager:
    def __init__(self, pygame):
        self.pygame = pygame
        self.frame = 0
        self.display_manager = Display_manager(pygame)
        self.sprite_manager = Sprite_manager(pygame)
        self.menu_manager = Menu_manager()

        self.display_manager.registerSpriteManager(self.sprite_manager)
        self.display_manager.registerMenuManager(self.menu_manager)

    def createSprite(self, image_type, image_name):
        sprite_behavior = image_type()
        sprite_initial_parameters = sprite_behavior.getInitialActions()

        sprite = Sprite(image_name)

        for action in sprite_initial_parameters:
            parameters = sprite_initial_parameters[action]
            sprite.applyAction(action, parameters)

        self.sprite_manager.registerSprite(sprite)

    def tick(self):
        if self.frame is 60:
            self.menu_manager.openMenu("start")
        self.display_manager.update()
        self.frame += 1
