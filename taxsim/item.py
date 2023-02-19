from termcolor import colored
import numpy as np


class Item:
    item_name = 'Generic item'

    def __init__(self):
        self.cell = None

    def tick(self):
        return


class Food(Item):
    item_name = 'Food'

    def __init__(self, nutrition=None):
        super().__init__()
        self.nutrition = nutrition or np.random.normal(10, 5)

    def tick(self):
        return

    def __repr__(self):
        return colored('*', 'white', 'on_yellow')


class Gold(Item):
    item_name = 'Gold'

    def __init__(self, value=None):
        super().__init__()
        self.value = value or np.random.normal(20, 3)

    def tick(self):
        return

    def __repr__(self):
        return colored('$', 'white', 'on_yellow')
