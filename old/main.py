import os
import time

from agent import GatherAgent
from item import Food, Poison
from world import World

if __name__ == '__main__':
    world = World(30, 30)
    agents = [GatherAgent(world) for _ in range(10)]

    items = []
    for _ in range(100):
        items.append(Food(world))
    for _ in range(5):
        items.append(Poison(world))

    world.draw()
    while True:
        world.tick()
        os.system('clear')
        world.draw()

        agents.sort(key=lambda agent: agent.energy, reverse=True)
        for index, agent in enumerate(agents):
            print(f'Agent {index}: {agent.energy} energy')

        time.sleep(0.3)
