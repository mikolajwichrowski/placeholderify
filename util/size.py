class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "{}{}".format(self.width, self.height)
