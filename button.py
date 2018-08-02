import pygame as pyg
from sprite import Sprite
from assets.fonts.fonts import Fonts

class Button(Sprite):
    def __init__(self, text = None, color = (0, 0, 0), initial_override = None):
        self.initial = {"translate": (0, 0), "scale": 0.1}

        Sprite.__init__(self, 'assets/sprites/button_case.png')

        if text is not None:
            self.rendered_text = Fonts().getFont("main").render(text, True, color)
            self.image.blit(self.rendered_text, self.calculateTextLocation())
            self.text = text

        if initial_override is not None:
            self.initial = initial_override
        else:
            self.initial = {"translate": (50, 50), "scale": 0.1}
        self.applyInitalActions()

    def getInitialActions(self):
        return self.initial

    def applyInitalActions(self):
        for action in self.initial:
            parameters = self.initial[action]
            self.external_actions[action](parameters)

    def calculateTextLocation(self):
        image_size = self.image.get_size()
        text_size = self.rendered_text.get_size()

        button_width, button_height = image_size[0], image_size[1]
        text_width, text_height = text_size[0], text_size[1]

        text_x = button_width / 2 - text_width / 2
        text_y = button_height / 2 - text_height / 2

        return text_x, text_y

