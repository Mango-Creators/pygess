from . import entity
from . import data
from . import colors
from . import physics
import time

# physics.prev_time = time.time()
def update():
    # physics.prev_time = time.time()
    physics.Dt = time.time() - physics.prev_time
    physics.prev_time = time.time()