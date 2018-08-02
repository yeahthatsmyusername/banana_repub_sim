class Menu:
    def __init__(self, menu_label):
        self.label = menu_label
        self.buttons = []
        self.texts = []

    def registerButton(self, button):
        self.buttons.append(button)

    def registerText(self, text):
        self.texts.append(text)

    def getSprites(self):
        all_sprites = []

        for text in self.texts:
            all_sprites.append(text)
        for button in self.buttons:
            all_sprites.append(button)

        return all_sprites