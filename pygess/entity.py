import pygame as pyg
from . import data
from . import physics
from . import colors

class Entity(pyg.sprite.DirtySprite):
    def __init__(self, position:tuple, dimensions:tuple, color=None, image_path=None) -> None:
        pyg.sprite.Sprite.__init__(self)
        
        self.pos = pyg.math.Vector2(position[0], position[1])
        self.dimensions = dimensions
        self.color = color
        
        if isinstance(image_path, str) and image_path != None:
            self.image = pyg.image.load(image_path).convert()
            self.image = pyg.transform.scale(self.image, self.dimensions)
        else:
            self.image = pyg.Surface(self.dimensions)
            self.image.fill(self.color)
        
        self.rect = self.image.get_frect()
        self.rect.topleft = self.pos
        
        self.spr_group = pyg.sprite.GroupSingle()
        self.spr_group.add(self)

        self._colliding_objects = []
        
        data.all_rects.append(self.rect)
    
    def update_rect(self):
        index = data.all_rects.index(self.rect)
        data.all_rects.remove(self.rect)
        
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        self.rect.width = self.dimensions[0]
        self.rect.height = self.dimensions[1]
        
    
        data.all_rects.insert(index + 1, self.rect)
    
    def check_collisions(self):
        for r in data.all_rects:
            if r == self.rect:
                continue
            if not self.rect.colliderect(r):
                continue
            
            else:
               if r in self._colliding_objects:
                self._colliding_objects.remove(r)
                continue
            
            if r not in self._colliding_objects:
                self._colliding_objects.append(r)
                continue
    
    def is_colliding_with(self, rect):
        return rect in self._colliding_objects

    def get_all_obj_colliding_with(self):
        return self._colliding_objects

    def update(self):
        self.check_collisions()
        self.update_rect()
        
        if self in self.spr_group:
            self.spr_group.remove(self)
            self.spr_group.update()
            self.spr_group.add(self)
        else:
            self.spr_group.update()
        
        self.spr_group.draw(pyg.display.get_surface())

class MovingEntity(Entity):
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color=None, image_path=None) -> None:
        Entity.__init__(self, position, dimensions, color, image_path)
        self.velocity = pyg.math.Vector2(velocity[0], velocity[1])

    def move(self):
        self.pos += self.velocity * physics.Dt
    
