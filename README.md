# About
This is a python library which aims at improving the use of the popular game development engine, pygame. Pygame is often confusing for beginners and a pain to type out all the boiler plate code. PyGess provides for multiple obvious, yet essential features that is frustrating to make always. This includes Entity classes like BasicEntity, RectEntity. Currently (as of v1.0.2) PyGess contains framerate independence, and gravity implementation. I am dedicated to this project and plan to add lots of more features and functionality.

# Installation
PyGess uses the default python package manager, pip to install. 

On Windows:
`python3 -m pip install pygess-py`

---
On Mac/Linux
`python3 -m pip3 install pygess-py`

To use: ```import pygess```

# Guide
## Entity Classes
- Basic Entity
- Rect Entity
- Basic Moving Entity
- Rect Moving Entity
- Basic Circular Entity
- Circular Moving Entity
- Sprite
- Moving Sprite

**Remember to use `pygess.update()`  at the start of your gameloop. This makes sure that deltatime is updated.**
### Basic Entity

```python
class BasicEntity:
    # Constructor
    def __init__(self, x_pos, y_pos, width, height) -> None:
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height

        self.surface = pyg.display.get_surface()
        self.rect = pyg.FRect(self.x, self.y, self.width, self.height)
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
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        data.all_rects.insert(index + 1, self.rect)

    # Update Function
    def update(self):
        self.update_rect()
        self.check_collisions()
```

**Parameters**: X position, Y position, Width, Height

This Entity is the superclass for all other types. It is invisible, but has a collider. The collider simply detects all the hitboxes of other entities that are in its hitbox. This data is stored in `self._colliding_objects` (List).
```python
    def update_rect(self):
	index = data.all_rects.index(self.rect)
        data.all_rects.remove(self.rect)
        
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        
        data.all_rects.insert(index + 1, self.rect)
```
  This  Function is responsible for updating the Rect information of it in the master hitbox list, `all_rects` .  All rects keeps track of all rectangles (used as hitboxes) created using PyGess classes.
### Rect Entity
```python
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
```
This is subclass of basic Entity. This makes the Entity visible in the form of a colored rectangle. It has the same functionality as BasicEntity with a draw function added. It also takes `color` as a parameter.
### Basic Moving Entity
(to be added)

## Guide Script
```python
    import pygame as pyg
    import pygess as gess
    import time
    
    
    if __name__ == "__main__":
        pyg.init()
        gess.physics.gravity = (0, 0)
        screen = pyg.display.set_mode((800, 900))
        
        # Entities
        ent1 = gess.entity.RectEntity(700, 600, 40, 40, gess.colors.GREEN)
        ent2 = gess.entity.BasicCircularEntity(300, 400, 20, gess.colors.RED)
        ent3 = gess.entity.MovingSprite(200, 300, 50, 50, "spri.png", (100, 0))
        ent4 = gess.entity.RectMovingEntity(200, 0, 20, 20, (20, 0), gess.colors.BLACK)
        
        # ent4 = gess.entity.Sprite(450, 550, 30, 30, "spri.png")
        
        font = pyg.font.SysFont(None, 30)
        
        # Loop
        is_running = True
        clock = pyg.time.Clock()
        
        gess.physics.prev_time = time.time()
        
        while is_running:
            gess.update()
            # gess.update()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    is_running = False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_SPACE:
                        ent4.vel_y = -500
            
            
            # Drawing
            screen.fill(gess.colors.WHITE)
            
            screen.blit(font.render(f"{gess.data.all_rects}", False, gess.colors.BLACK), (20, 20))
            screen.blit(font.render(f"{gess.physics.Dt}", False, gess.colors.BLACK), (20, 40))
            screen.blit(font.render(f"{clock.get_fps()}", False, gess.colors.BLACK), (20, 60))
            
            ent1.update()
            pyg.draw.rect(screen, gess.colors.BLUE, ent2.rect)
            ent2.update()
            pyg.draw.rect(screen, gess.colors.BLACK, ent3.rect)2
            ent3.update()
            ent4.update()
            
            # Update
            pyg.display.update()
            pyg.display.flip()
            
            # clock.tick(120);
```

