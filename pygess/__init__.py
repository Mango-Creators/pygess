from . import entity
from . import data
from . import colors
from . import physics
from . import entity
import time


__version__ = '1.0.1'

# physics.prev_time = time.time()
def update():
    # physics.prev_time = time.time()
    physics.Dt = time.time() - physics.prev_time
    physics.prev_time = time.time()