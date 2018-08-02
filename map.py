class Map:
    def __init__(self):
        self.initial = {"translate": (-100, -100), "scale": 0.3}

    def getInitialActions(self):
        return self.initial