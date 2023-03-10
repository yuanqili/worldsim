import os
import time

from taxsim.world import World


class Driver:

    def __init__(self, rows, cols):
        self.world = World(rows, cols)

    def run(self, tick_time=0.1):
        round = 0
        while True:
            round += 1
            print(f'AI Economist – Round: {round}')
            self.world.draw()
            self.world.tick()
            time.sleep(tick_time)
            self.clear()

    @staticmethod
    def clear():
        os.system('clear')
