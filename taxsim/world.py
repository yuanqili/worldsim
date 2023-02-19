from perlin_noise import PerlinNoise

from taxsim.cell import Cell
from taxsim.enums import Direction
from taxsim.terrain import Plain, Water, Fertile, Mountain


class World:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col, self) for col in range(cols)] for row in range(rows)]
        self.generate_map()

    def generate_map(self, concave=2):
        noise = PerlinNoise(concave)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                value = noise([row / self.rows, col / self.cols])
                if value < -0.2:
                    cell.terrain = Water(cell)
                elif value < 0:
                    cell.terrain = Fertile(cell)
                elif value < 0.3:
                    cell.terrain = Plain(cell)
                else:
                    cell.terrain = Mountain(cell)

    def tick(self):
        for row in self.cells:
            for cell in row:
                cell.tick()

    def draw(self):
        for row in self.cells:
            for cell in row:
                print(cell, end=' ')
            print()

    def move(self, direction, agent):
        match direction:
            case Direction.UP:
                row = agent._cell.row - 1
                col = agent._cell.col
            case Direction.DOWN:
                row = agent._cell.row + 1
                col = agent._cell.col
            case Direction.LEFT:
                row = agent._cell.row
                col = agent._cell.col - 1
            case Direction.RIGHT:
                row = agent._cell.row
                col = agent._cell.col + 1
        return self.is_position_valid(row, col) and self.cells[row][col].add_agent(agent)

    def is_position_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
