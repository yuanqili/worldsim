from termcolor import colored


class Cell:
    cell_name = 'Cell'

    def __init__(self, row, col, world=None, terrain=None):
        self.row = row
        self.col = col
        self.world = world

        self.terrain = terrain
        self.items = []
        self.agents = []

    def add_item(self, item):
        if item.cell is None:
            item.cell = self
        self.items.append(item)

    def add_agent(self, agent):
        self.agents.append(agent)

    def tick(self):
        self.terrain.tick()
        for item in self.items:
            item.tick()
        for agent in self.agents:
            agent.tick()

    def __repr__(self):
        if len(self.items) > 0:
            return colored('I', 'yellow', 'on_green')
        return str(self.terrain)
