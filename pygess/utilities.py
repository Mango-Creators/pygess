from pygess import entity
from pygess import physics
import pygame as pyg
import copy

def instantiate(entity: entity.Entity, world: physics.World, pos:pyg.Vector2=None):
    entity_instance = copy.deepcopy(entity)
    entity_instance.pos = pos if pos else entity_instance.pos
    world.load_new_object(entity_instance)

def get_key_pressed(key):
    keys = pyg.key.get_pressed()
    if key in keys:
        return True
    return False