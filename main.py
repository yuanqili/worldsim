#!/usr/bin/env python3
import random

from taxsim.agent import Human
from taxsim.driver import Driver

if __name__ == '__main__':
    driver = Driver(40, 80)
    agents = []
    for _ in range(20):
        row = random.randint(0, driver.world.rows - 1)
        col = random.randint(0, driver.world.cols - 1)
        agent = Human()
        driver.world.cells[row][col].add_agent(agent)
        agents.append(agent)
    print(agents)
    driver.run(0.5)
