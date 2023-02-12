import random

from termcolor import colored


class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[None for _ in range(width)] for _ in range(height)]
        self.cells = []

    def add_cell(self, cell):
        if self.map[cell.y][cell.x] is not None:
            return False
        self.cells.append(cell)
        self.map[cell.y][cell.x] = cell
        return True

    def remove_cell(self, cell):
        self.cells.remove(cell)
        self.map[cell.y][cell.x] = None

    def tick(self):
        for cell in self.cells:
            cell.tick()

    def draw(self):
        for row in self.map:
            for cell in row:
                if cell is None:
                    print(colored('.', 'light_grey'), end=' ')
                else:
                    print(cell, end=' ')
            print()

    def is_position_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_empty(self, x, y):
        return self.is_position_valid(x, y) and self.map[y][x] is None

    def random_empty_position(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map[y][x] is None:
                return x, y
