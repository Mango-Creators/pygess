import pygame as pyg
from . import data


# Basic Entity
class BasicEntity:
    # Constructor
    def __init__(self, x_pos, y_pos, width, height) -> None:
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height

        self.surface = pyg.display.get_surface()
        self.rect = pyg.Rect(self.x, self.y, self.width, self.height)
        # self.prev_rect = pyg.Rect(self.x, self.y, self.width, self.height)
        
        self._colliding_objects = []

        if self.rect not in data.all_rects:
            data.all_rects.append(self.rect)

    # Checks what all objects are colliding with itself
    def check_collisions(self):
        for r in data.all_rects:
            if r == self.rect:
                continue
            if self.rect.colliderect(r):
                if r not in self._colliding_objects:
                    self._colliding_objects.append(r)
            else:
                if r in self._colliding_objects:
                    self._colliding_objects.remove(r)

    # Resturns the colliding objects list
    def get_colliding_objects(self) -> list:
        return self._colliding_objects

    def update_rect(self):
        index = data.all_rects.index(self.rect)
        data.all_rects.remove(self.rect)
        self.rect = pyg.Rect(self.x, self.y, self.width, self.height)
        data.all_rects.insert(index + 1, self.rect)

    # Update Function
    def update(self):
        self.update_rect()
        self.check_collisions()


# Rectangle Entity
class RectEntity(BasicEntity):
    # Super constructor
    def __init__(self, x_pos, y_pos, width, height, color) -> None:
        BasicEntity.__init__(self, x_pos, y_pos, width, height)
        self.color = color

    # New Draw function added
    def _draw(self):
        pyg.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        self.update_rect()
        self.check_collisions()
        self._draw()


# Basic Moving Entity
class MovingBasicEntity(BasicEntity):
    def __init__(self, x_pos, y_pos, width, height, velocity: tuple) -> None:
        BasicEntity.__init__(self, x_pos, y_pos, width, height)
        self.vel_x = velocity[0]
        self.vel_y = velocity[1]
    
    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def update(self):
        self.move()
        self.update_rect()
        self.check_collisions()


# Rectangle Moving Entity
class MovingRectEntity(MovingBasicEntity, RectEntity):
    def __init__(self, x_pos, y_pos, width, height, velocity, color: tuple) -> None:
        MovingBasicEntity.__init__(self, x_pos, y_pos, width, height, velocity)
        RectEntity.__init__(self, x_pos, y_pos, width, height, color)
    
    def update(self):
        self.move()
        self.update_rect()
        self.check_collisions()
        self._draw()  # Call the draw method from RectEntity


# Basic Circular Entity
class BasicCircularEntity(RectEntity):
    def __init__(self, center_x, center_y, radius, color) -> None:
        
        self.centerx = center_x
        self.centery = center_y
        self.radius = radius
        
        self.color = color
        # ((self.radius/2) - self.radius)
        self.rect_coords = [self.centerx - self.radius, self.centery - self.radius]
        self.rect_side = radius * 1.7
        
        RectEntity.__init__(self, self.rect_coords[0], self.rect_coords[1], self.rect_side, self.rect_side, self.color)
    
    def _draw(self):
        pyg.draw.circle(self.surface, self.color, (self.centerx, self.centery), self.radius)
    
    def update_rect(self):
        # Remove earlier rect
        index = data.all_rects.index(self.rect)
        data.all_rects.remove(self.rect)
        
        # Update rect
        self.rect.center = (self.centerx, self.centery)
        self.rect.width = self.width
        self.rect.height = self.height
        
        # Add new rect
        data.all_rects.insert(index + 1, self.rect)


# Circular Moving Entity
class CircularMovingEntity(BasicCircularEntity, MovingBasicEntity):
    def __init__(self, center_x, center_y, radius, velocity: tuple, color) -> None:
        BasicCircularEntity.__init__(self, center_x, center_y, radius, color)
        MovingBasicEntity.__init__(self, self.rect.x, self.rect.y, self.width, self.height, velocity)
    
    def move(self):
        self.centerx += self.vel_x
        self.centery += self.vel_y
        
    def update(self):
        self.check_collisions()
        self.move()
        self.update_rect()
        self._draw()
    
    

