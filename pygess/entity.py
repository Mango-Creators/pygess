import pygame as pyg
from pygess import data
from pygess import physics
import uuid

class Entity(pyg.sprite.DirtySprite):
    def __init__(self, position: tuple, dimensions: tuple, color=None, image_path=None) -> None:
    
        pyg.sprite.DirtySprite.__init__(self)
        self.pos = pyg.math.Vector2(position)
        self.dimensions = dimensions
        self.color = color
        
        self.parent = None
        self.id = uuid.uuid4()
        self.__is_instance = False

        self.active_world = physics.get_active_world()
        
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
        self.active_world = physics.get_active_world()

        self.update_rect()
        self.check_collisions()
        
        if self in self.spr_group:
            self.spr_group.remove(self)
            self.spr_group.update()
            self.spr_group.add(self)
        else:
            self.spr_group.update()
            
        self.spr_group.draw(pyg.display.get_surface())
    
    
        
class MovingEntity(Entity):
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color:tuple=None, image_path=None) -> None:
        super().__init__(position, dimensions, color=color, image_path=image_path)
        self.velocity = pyg.math.Vector2(velocity)
        self.orignal_vel = pyg.math.Vector2(velocity)
        self.is_affected_by_gravity = False

    def update(self):
        self.active_world = physics.get_active_world()

        self.update_rect()
        self.check_collisions()
        self.move()
        
        if self in self.spr_group:
            self.spr_group.remove(self)
            self.spr_group.update()
            self.spr_group.add(self)
        else:
            self.spr_group.update()
            
        self.spr_group.draw(pyg.display.get_surface())
        
    def move(self):
        self.pos += self.velocity * physics.delta_time;
        
        if not self.is_affected_by_gravity:
            self.velocity.y = 0
            return
        
        self.velocity += self.active_world.gravity
        
    def set_gravitified(self, bool:bool):
        self.is_affected_by_gravity = bool
        