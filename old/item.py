import random

from termcolor import colored

from cell import Cell


class Item(Cell):

    def __init__(self, world, x, y):
        super().__init__(x, y)
        self.add(world)

    def tick(self):
        raise NotImplementedError

    def __str__(self):
        return colored('I', 'red')


class Food(Item):

    def __init__(self, world):
        x, y = world.random_empty_position()
        super().__init__(world, x, y)
        self.energy = int(random.randint(10, 15))

    def tick(self):
        self.energy -= 1
        if self.energy <= 0:
            self.remove()

    def __str__(self):
        return colored('F', 'green')


class Poison(Item):

    def __init__(self, world):
        x, y = world.random_empty_position()
        super().__init__(world, x, y)
        self.energy = -10

    def tick(self):
        pass

    def __str__(self):
        return colored('P', 'red')
