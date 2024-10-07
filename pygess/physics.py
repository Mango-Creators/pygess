import math as mt
import time
import uuid
import pygame as pyg
import copy

from pygame.sprite import Sprite
from pygess import data

worlds = []

delta_time = 0.001
__prev_time = time.time()


class GameObjects:
    """
    # Description
    A class which stores list of Entities. Also updates them.
    Basically a sprite group for entities instead.

    # Functions
    ## Init
    ```
    def __init__(self, entities:list) -> None:
        self.entities = entities
    ```
    Initializes entity list.

    ## update
    ```
    def update(self):
        from . import entity as ent
        self.entities = list(set(self.entities))
        for entity in self.entities:
            if isinstance(entity, (ent.Entity)):
                entity.update()
    ```
    Updates all entities in list.

    """

    def __init__(self, entities: list) -> None:
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
        self.is_active = False

        self.__objects = GameObjects(list(game_objects))
        self.runtime_objs: GameObjects = None;
        
        # Counters
        self.__init_runtime_counter = 0

        worlds.append(self)

    def update(self):
        if self.__init_runtime_counter == 0:
            self.runtime_objs = copy.deepcopy(self.__objects)
            for x in self.runtime_objs.entities:
                x.__is_instance = True

        self.runtime_objs.update()

        # If statement to save memory and stop counter
        if self.__init_runtime_counter < 2:   
            self.__init_runtime_counter += 1;

    def add_gameobj(self, *gameobj):
        for obj in gameobj:
            self.__objects.append(obj)

    def load_new_object(self, *gameobj):
        for obj in gameobj:
            self.runtime_objs.append(obj)



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


def set_active_world(world: World):
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


def first_instance_of_prefab_in_world(world, prefab_entity) -> "entity.Entity":
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            return e


def all_instances_of_prefab_in_world(world, prefab_entity) -> list:
    instances = []
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            instances.append(e)

    return instances


def update_delta_time():
    global delta_time
    global __prev_time
    
    delta_time = min(time.time()-__prev_time, 0.1);
    __prev_time = time.time()
