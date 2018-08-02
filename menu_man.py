from button import Button
from menu import Menu

class Menu_manager:
    def __init__(self):
        self.menu_is_active = False
        self.active_menu = None
        self.all_menus = {}
        start_menu = Menu("start")

        b_1 = Button("Play", initial_override={"translate": (200, 100), "scale": 0.25})
        b_2 = Button("Settings", initial_override={"translate": (200, 200), "scale": 0.25})
        b_3 = Button("Achievements", initial_override={"translate": (200, 300), "scale": 0.25})
        b_4 = Button("Exit Game", initial_override={"translate": (200, 400), "scale": 0.25})

        start_menu.registerButton(b_1)
        start_menu.registerButton(b_2)
        start_menu.registerButton(b_3)
        start_menu.registerButton(b_4)

        self.addMenu("start", start_menu)

    def openMenu(self, menu_name):
        self.menu_is_active = True
        self.active_menu = self.all_menus[menu_name]

    def addMenu(self, menu_name, menu):
        self.all_menus[menu_name] = menu

    def getActiveMenu(self):
        if self.menu_is_active:
            return self.all_menus[self.active_menu]
        else:
            return False

    def getActiveMenuSprites(self):
        if self.menu_is_active:
            return self.active_menu.getSprites()
        else:
            return []