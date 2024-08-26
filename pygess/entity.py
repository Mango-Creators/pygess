import pygame as pyg
from . import data
from . import physics

class Entity(pyg.sprite.DirtySprite):
    def __init__(self, position: tuple, dimensions: tuple, color=None, image_path=None) -> None:
        pyg.sprite.DirtySprite.__init__(self)
        self.pos = pyg.math.Vector2(position)
        self.dimensions = dimensions
        self.color = color
        
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
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color=None, image_path=None) -> None:
        Entity.__init__(self, position, dimensions, color, image_path)
        self.velocity = pyg.math.Vector2(velocity)

    def move(self):
        self.pos += self.velocity * physics.Dt
