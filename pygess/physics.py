import math as mt
import time
import pygame as pyg

worlds = []

class World:
    def __init__(self, grav: tuple) -> None:
        self.gravity = pyg.math.Vector2(grav)
        self.dt = 0
        self.prev_time = time.time()
        self.is_active = False
        
        worlds.append(self)
        
    
    def update_delta_time(self):

        if self.is_active: 
            self.dt = time.time() - self.prev_time
            self.prev_time = time.time()
            return
        self.dt = get_active_world().dt
        self.dt = min(self.dt, 0.1)

def get_active_world():
    for world in worlds:
        if world.is_active:
            return world

def _debug_no_active_worlds():
    counter = 0
    
    for world in worlds:
        if world.is_active:
            counter += 1
    
    return counter

def set_active_world(world:World):
    if _debug_no_active_worlds() > 0:
        get_active_world().is_active = False
        
    world.is_active = True

def get_all_worlds():
    return worlds
