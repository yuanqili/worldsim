class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.world = None

    def add(self, world):
        self.world = world
        return self.world.add_cell(self)

    def remove(self):
        self.world.remove_cell(self)

    def distance_to(self, other, order=1):
        return ((self.x - other.x) ** order + (self.y - other.y) ** order) ** (1 / order)

    def direction_to(self, other):
        if self.x < other.x:
            x = 1
        elif self.x > other.x:
            x = -1
        else:
            x = 0
        if self.y < other.y:
            y = 1
        elif self.y > other.y:
            y = -1
        else:
            y = 0
        return x, y
