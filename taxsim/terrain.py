import abc
import random

from termcolor import colored

from taxsim.item import Food


class Terrain(abc.ABC):
    terrain_name = 'Generic terrain'

    def __init__(self, cell):
        self.cell = cell

    @abc.abstractmethod
    def tick(self):
        return

    @abc.abstractmethod
    def __repr__(self):
        return


class Plain(Terrain):
    terrain_name = 'Plain'

    def __init__(self, cell):
        super().__init__(cell)

    def tick(self):
        return

    def __repr__(self):
        return colored('.', 'green')


class Water(Terrain):
    terrain_name = 'Water'

    def __init__(self, cell):
        super().__init__(cell)

    def tick(self):
        return

    def __repr__(self):
        return colored('~', 'blue')


class Fertile(Terrain):
    terrain_name = 'Fertile'
    TERRAIN_FERTILE_DEFAULT_PROB = 0.1
    TERRAIN_FERTILE_DEFAULT_CYCLE = 20

    def __init__(self, cell):
        super().__init__(cell)
        self.prob = Fertile.TERRAIN_FERTILE_DEFAULT_PROB
        self.cycle = Fertile.TERRAIN_FERTILE_DEFAULT_CYCLE

    def tick(self):
        self.cycle -= 1
        if self.cycle > 0:
            return

        if random.random() < self.prob:
            self.cell.add_item(Food())
            self.prob = Fertile.TERRAIN_FERTILE_DEFAULT_PROB
        else:
            if self.prob <= 0.3:
                self.prob += 0.02
        self.cycle = Fertile.TERRAIN_FERTILE_DEFAULT_CYCLE

    def __repr__(self):
        return colored('*', 'yellow')


class Mountain(Terrain):
    terrain_name = 'Mountain'

    def __init__(self, cell):
        super().__init__(cell)

    def tick(self):
        return

    def __repr__(self):
        return colored('%', 'magenta')
