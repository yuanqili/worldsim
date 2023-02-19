import abc
import random

from termcolor import colored

from taxsim.cell import Cell
from taxsim.enums import Direction
from taxsim.item import Food


class Agent(abc.ABC):
    agent_name = 'Generic agent'

    def __init__(self):
        self._cell: Cell | None = None

    def set_cell(self, cell: Cell):
        # print(f'Agent.set_cell() to {cell} ({cell.row}, {cell.col})')
        self._cell = cell

    def get_cell(self) -> Cell:
        return self._cell

    @abc.abstractmethod
    def tick(self):
        return

    @abc.abstractmethod
    def __repr__(self):
        return


class Human(Agent):
    agent_name = 'Human'

    def __init__(self, health=100):
        super().__init__()
        self.health = health

    def move(self):
        if random.random() < 0.25:
            return self._cell.move(Direction.UP, self)
        elif random.random() < 0.5:
            return self._cell.move(Direction.DOWN, self)
        elif random.random() < 0.75:
            return self._cell.move(Direction.LEFT, self)
        else:
            return self._cell.move(Direction.RIGHT, self)

    def tick(self):
        # if there is food in the current cell
        if (food := self._cell.get_first_item(Food)) is not None:
            self.health += food.nutrition
            self._cell.remove_item(food)
        # otherwise, move around
        else:
            self.move()

    def __repr__(self):
        return colored('@', 'white', 'on_green')
