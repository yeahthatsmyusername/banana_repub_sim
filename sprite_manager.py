class Sprite_manager:
    sprites_list = []

    def __init__(self, pygame):
        self.pygame = pygame

    def registerSprite(self, sprite):
        Sprite_manager.sprites_list.append(sprite)

    def getSprites(self):
        return Sprite_manager.sprites_list