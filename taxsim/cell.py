from taxsim.item import Food
from taxsim.terrain import Water


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
        item._cell = self
        self.items.append(item)

    def remove_item(self, item):
        item._cell = None
        self.items.remove(item)

    def get_first_item(self, klass):
        items = list(filter(lambda item: isinstance(item, klass), self.items))
        return items[0] if items else None

    def add_agent(self, agent):
        # CONDITION: if the cell is not a water cell
        if isinstance(self.terrain, Water):
            return False
        # CONDITION: if the cell does not contain anything but food
        if self.items and any(not isinstance(item, Food) for item in self.items):
            return False
        # CONDITION: if the cell does not contain any agents
        if self.agents:
            return False

        # add the agent to the cell
        agent.set_cell(self)
        self.agents.append(agent)
        return True

    def remove_agent(self, agent):
        # agent.set_cell(None)
        self.agents.remove(agent)

    def tick(self):
        self.terrain.tick()
        for item in self.items:
            item.tick()
        for agent in self.agents:
            agent.tick()

    def move(self, direction, agent):
        if not self.world.move(direction, agent):
            return False
        self.remove_agent(agent)
        return True

    def __repr__(self):
        if self.agents:
            return str(self.agents[0])
        elif self.items:
            return str(self.items[0])
        else:
            return str(self.terrain)
