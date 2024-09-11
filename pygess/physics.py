import math as mt
import time
import uuid
import pygame as pyg
import copy
from . import data

worlds = []

class GameObjects:
    def __init__(self, entities:list) -> None:
        self.entities = entities
        
    def update(self):
        from . import entity as ent
        self.entities = list(set(self.entities))
        for entity in self.entities:
            if isinstance(entity, (ent.Entity)):
                entity.update()
            
    def append(self, *entity):
        for e in entity:
            if e != None:
                self.entities = list(self.entities)
                self.entities.append(e)

class World:
    def __init__(self, grav: tuple, *game_objects) -> None:
        self.gravity = pyg.math.Vector2(grav)
        self.dt = 0
        self.prev_time = time.time()
        self.is_active = False
        
        self.__counter = 0
        self.__counter2 = 0
        
        self.__objects = GameObjects(game_objects)
        self.runtime_obj = copy.deepcopy(self.__objects)
        self.__base_state = self.runtime_obj
        
        worlds.append(self)
        
    def update(self):
        if not self.is_active:
            self.__counter2 = 0
            return
        
        if self.__counter2 == 0:
            self.__reset()
        
        if self.__counter == 0:
            self.__set_runtime()

        self.runtime_obj.update()
        
        self.__counter += 1
        self.__counter2 += 1
    
    def add_gameobj(self, *gameobj):
        for obj in gameobj:
            self.__objects.append(obj)
    
    def load_new_object(self, *gameobj):
        for obj in gameobj:
            self.runtime_obj.append(obj)
        
    def update_delta_time(self):

        if self.is_active: 
            self.dt = min(time.time() - self.prev_time, 0.1)
            self.prev_time = time.time()
            return
        self.dt = get_active_world().dt
        self.dt = min(self.dt, 0.1)
    
    def __set_runtime(self):
        ent = []
        for e in self.__objects.entities:
            if e.rect not in data.all_rects:
                data.all_rects.append(e.rect)
            en = copy.deepcopy(e)
            en.id = uuid.uuid4()
            en.parent = e
            ent.append(copy.deepcopy(en))
        
        self.runtime_obj = GameObjects(ent)
        self.__base_state = GameObjects(copy.deepcopy(ent))
        
    def __reset(self):
        ent = []
        for e in self.__base_state.entities:
            if e.rect not in data.all_rects:
                data.all_rects.append(e.rect)
            ent.append(copy.deepcopy(e))
        
        self.runtime_obj = GameObjects(ent)

    def _deactivate(self):
        self.is_active = False
    
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
        get_active_world()._deactivate()
        
        
    world.is_active = True

def get_all_worlds():
    return worlds

def update_delta_time():
    for w in get_all_worlds():
        w.update_delta_time()

def update_worlds():
    for w in get_all_worlds():
        w.update()

def first_instance_of_prefab_in_world(world, prefab_entity) -> 'entity.Entity':
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            return e

def all_instances_of_prefab_in_world(world, prefab_entity) -> list:
    instances = []
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            instances.append(e)
    
    return instances