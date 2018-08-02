import pygame as pyg
import sys
from pygame.locals import *
from game_manager import Game_manager
from map import Map
from button import Button
from assets.fonts.fonts import Fonts

width, height = 100, 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
r, g, b = 0, 0, 0
DEBUG = False

pyg.init()
clock = pyg.time.Clock()
pyg.mouse.set_visible(not DEBUG)

fonts = Fonts()
main_font = fonts.getFont("main")

game_manager = Game_manager(pyg)
game_manager.createSprite(Map, "assets/sprites/map.png")
game_manager.createSprite(Button, "assets/sprites/next_turn_sprites/sprite_00.png")

b_1 = main_font.render("Confirm", True, BLACK)
b_2 = main_font.render("Cancel", True, BLACK)





while True:
    game_manager.tick()

    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            sys.exit()