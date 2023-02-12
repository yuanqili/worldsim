import random

from termcolor import colored

from cell import Cell
from item import Food


class Agent(Cell):

    def __init__(self, world, x, y):
        super().__init__(x, y)
        self.add(world)

    def tick(self):
        raise NotImplementedError

    def __str__(self):
        return colored('A', 'blue', attrs=['bold'])


class RandomAgent(Agent):

    def tick(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        if self.world.is_position_empty(self.x + x, self.y + y):
            self.world.map[self.y][self.x] = None
            self.x += x
            self.y += y
            self.world.map[self.y][self.x] = self


class ClusterAgent(Agent):

    def tick(self):
        world_agents = self.world.agents

        # find the closest agent to self
        closest_agent = None
        closest_distance = None
        for agent in world_agents:
            if agent is not self:
                distance = abs(self.x - agent.x) + abs(self.y - agent.y)
                if closest_distance is None or distance < closest_distance:
                    closest_agent = agent
                    closest_distance = distance

        # move to the closest agent
        if closest_agent is not None:

            if self.x < closest_agent.x:
                x = 1
            elif self.x > closest_agent.x:
                x = -1
            else:
                x = 0

            if self.y < closest_agent.y:
                y = 1
            elif self.y > closest_agent.y:
                y = -1
            else:
                y = 0

            if self.world.is_position_empty(self.x + x, self.y + y):
                self.world.map[self.y][self.x] = None
                self.x += x
                self.y += y
                self.world.map[self.y][self.x] = self


class GatherAgent(Agent):
    """
    GatherAgent aims to find as much food as it can
    """

    def __init__(self, world):
        x, y = world.random_empty_position()
        super().__init__(world, x, y)
        self.energy = 10

    def tick(self):
        # find the closest food
        closest_food: Cell = None
        closest_distance = None
        for food in filter(lambda cell: isinstance(cell, Food), self.world.cells):
            distance = self.distance_to(food)
            if closest_distance is None or distance < closest_distance:
                closest_food = food
                closest_distance = distance

        # move to the closest food
        if closest_food is not None:
            x, y = self.direction_to(closest_food)
            if self.world.is_position_empty(self.x + x, self.y + y):
                self.world.map[self.y][self.x] = None
                self.x += x
                self.y += y
                self.world.map[self.y][self.x] = self

        # eat food
        if closest_food is not None:
            if closest_distance <= 1:
                self.energy += closest_food.energy
                closest_food.remove()

        # die
        self.energy -= 1
        if self.energy <= 0:
            self.remove()

    def __str__(self):
        return colored('G', 'yellow', attrs=['bold'])
