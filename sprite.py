import math
import pygame as pyg
class Sprite:
    def __init__(self, image_name):
        self.pygame = pyg
        self.image = self.pygame.image.load(image_name)
        self.position = {"x": 0, "y": 0}
        self.internal_size = self.image.get_size()
        self.external_actions = {"translate": self.translate, "scale": self.scale}
        #self.active = False

    def getPosition(self):
        return (self.position["x"], self.position["y"])

    def translate(self, translation):
        self.old_x = self.position["x"]
        self.old_y = self.position["y"]
        self.new_x = self.old_x + translation[0]
        self.new_y = self.old_y + translation[1]
        self.position = {"x": self.new_x, "y": self.new_y}

    def scale(self, scaling_factor):
        old_size = self.internal_size
        new_size = (old_size[0] * scaling_factor, old_size[1] * scaling_factor)
        self.internal_size = new_size
        self.external_size = (math.floor(self.internal_size[0]), math.floor(self.internal_size[1]))
        self.image = self.pygame.transform.scale(self.image, self.external_size)

    def applyAction(self, action_name, parameters):
        self.external_actions[action_name](parameters)

    #def makeActive(self):
        #self.active = True

    #def isActive(self):
        #return self.active
