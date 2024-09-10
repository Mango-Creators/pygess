import math as mt
import time
import pygame as pyg

worlds = []

class GameObjects:
    def __init__(self, entities:tuple) -> None:
        self.entities = entities
        
    def update(self):
        from . import entity as ent
        self.entities = tuple(set(self.entities))
        for entity in self.entities:
            if isinstance(entity, (ent.Entity)):
                entity.update()
            
    def append(self, entity: tuple):
        for e in entity:
            if e != None:
                a = list(self.entities)
                a.append(e)
                self.entities = tuple(a)

class World:
    def __init__(self, grav: tuple, game_objects: tuple = ()) -> None:
        self.gravity = pyg.math.Vector2(grav)
        self.dt = 0
        self.prev_time = time.time()
        self.is_active = False
        
        self.objects = GameObjects(game_objects)
        
        worlds.append(self)
        
    def update(self):
        self.objects.update()
    
    def add_gameobj(self, gameobj: tuple):
        for obj in gameobj:
            self.objects.append((obj,))
        
    def update_delta_time(self):

        if self.is_active: 
            self.dt = time.time() - self.prev_time
            self.prev_time = time.time()
            return
        self.dt = get_active_world().dt
        self.dt = min(self.dt, 0.1)

def get_active_world() -> World:
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
