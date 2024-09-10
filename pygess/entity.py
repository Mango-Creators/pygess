import pygame as pyg
from . import data
from . import physics

class Entity(pyg.sprite.DirtySprite):
    def __init__(self, position: tuple, dimensions: tuple, color=None, image_path=None) -> None:
        pyg.sprite.DirtySprite.__init__(self)
        self.pos = pyg.math.Vector2(position)
        self.dimensions = dimensions
        self.color = color
        
        self.worlds_to_exist = []
        self.current_world: physics.World = None
        self.previous_world = None
        
        if isinstance(image_path, str) and image_path:
            self.image = pyg.image.load(image_path).convert()
            self.image = pyg.transform.scale(self.image, self.dimensions)
        else:
            self.image = pyg.Surface(self.dimensions)
            self.image.fill(self.color)
        
        self.rect = self.image.get_frect(topleft=self.pos)
        
        self.spr_group = pyg.sprite.GroupSingle()
        self.spr_group.add(self)

        self._colliding_objects = []
        
        data.all_rects.append(self.rect)
    
    def update_rect(self):
        index = data.all_rects.index(self.rect)
        data.all_rects.remove(self.rect)
        
        self.rect.topleft = self.pos
        self.rect.size = self.dimensions
        
        data.all_rects.insert(index, self.rect)
    
    def check_collisions(self):
        self._colliding_objects = [r for r in data.all_rects if r != self.rect and self.rect.colliderect(r)]
    
    def is_colliding_with(self, rect):
        return rect in self._colliding_objects

    def get_all_obj_colliding_with(self):
        return self._colliding_objects

    def update(self):
        self.update_current_world()
        
        if self.current_world:
            self.update_rect()
            self.check_collisions()
            
            if self in self.spr_group:
                self.spr_group.remove(self)
                self.spr_group.update()
                self.spr_group.add(self)
            else:
                self.spr_group.update()
                
            self.spr_group.draw(pyg.display.get_surface())
            return

        return
    
    def set_worlds_to_exist(self, *argv: physics.World):
        for world in argv:
            if world not in physics.get_all_worlds():
                print("Unregistered World!")
                continue
            
            self.worlds_to_exist.append(world)
    
    def update_current_world(self):
        active_world = physics.get_active_world()
            
        if active_world in self.worlds_to_exist:
            if active_world != self.current_world:
                self.previous_world = self.current_world
            self.current_world = active_world
        else:
            self.current_world = None
    
        
class MovingEntity(Entity):
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color=None, image_path=None) -> None:
        Entity.__init__(self, position, dimensions, color, image_path)
        self.velocity = pyg.math.Vector2(velocity)
        self.orignal_vel = pyg.math.Vector2(velocity)
        self.is_affected_by_gravity = False

    def move(self):
        if self.current_world == None:
            return
        self.pos += self.velocity * self.current_world.dt
        
        if not self.is_affected_by_gravity:
            return
        
        self.velocity += self.current_world.gravity
        
    def set_gravitified(self, bool:bool):
        self.is_affected_by_gravity = bool
        
    def update_current_world(self):
        active_world = physics.get_active_world()
            
        if active_world in self.worlds_to_exist:
            if active_world != self.current_world:
                self.previous_world = self.current_world
                self.velocity = self.orignal_vel
            self.current_world = active_world
        else:
            self.current_world = None