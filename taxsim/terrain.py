import abc
import os
import random

from dotenv import load_dotenv, dotenv_values
from termcolor import colored

from taxsim.item import Food, Gold

load_dotenv()


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

    def __init__(self, cell):
        super().__init__(cell)
        self.prob = float(os.environ.get('TERRAIN_FERTILE_FOOD_DEFAULT_PROB', 0.1))
        self.cycle = int(os.environ.get('TERRAIN_FERTILE_FOOD_DEFAULT_CYCLE', 10))

    def tick(self):
        self.cycle -= 1
        if self.cycle > 0:
            return
        if random.random() < self.prob:
            # TODO: may need to check if the cell is full
            self.cell.add_item(Food())
            self.prob = float(os.environ.get('TERRAIN_FERTILE_FOOD_DEFAULT_PROB', 0.1))
        else:
            if self.prob <= 0.3:
                self.prob += 0.02
        self.cycle = int(os.environ.get('TERRAIN_FERTILE_FOOD_DEFAULT_CYCLE', 10))

    def __repr__(self):
        return colored('*', 'yellow')


class Mountain(Terrain):
    terrain_name = 'Mountain'

    def __init__(self, cell):
        super().__init__(cell)
        self.prob = float(os.environ.get('TERRAIN_MOUNTAIN_GOLD_DEFAULT_PROB', 0.1))
        self.cycle = int(os.environ.get('TERRAIN_MOUNTAIN_GOLD_DEFAULT_CYCLE', 10))

    def tick(self):
        self.cycle -= 1
        if self.cycle > 0:
            return
        if random.random() < self.prob:
            # TODO: may need to check if the cell is full
            self.cell.add_item(Gold())
            self.prob = float(os.environ.get('TERRAIN_MOUNTAIN_GOLD_DEFAULT_PROB', 0.1))
        else:
            if self.prob <= 0.3:
                self.prob += 0.02
        self.cycle = int(os.environ.get('TERRAIN_MOUNTAIN_GOLD_DEFAULT_CYCLE', 10))

    def __repr__(self):
        return colored('%', 'magenta')
