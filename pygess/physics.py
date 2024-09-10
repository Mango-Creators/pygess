import math as mt
import time

class World:
    def __init__(self, grav: tuple) -> None:
        self.gravity = grav
        self.dt = 0
        self.prev_time = time.time()
