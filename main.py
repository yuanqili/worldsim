#!/usr/bin/env python3

from taxsim.driver import Driver

if __name__ == '__main__':
    driver = Driver(40, 120)
    driver.run(0.5)
