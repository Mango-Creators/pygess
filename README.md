---
title: 'Guide: How to use PyGess'
---
# Introduction

This document will walk you through the implementation of the PyGess library.

PyGess is a physics engine designed to manage game objects, their interactions, and their updates within a game world. It provides classes and functions to handle entities, game objects, and worlds, along with utility functions to manage these components.

We will cover:

1. The <SwmToken path="/pygess/physics.py" pos="10:2:2" line-data="class GameObjects:">`GameObjects`</SwmToken> class and its methods.
2. The <SwmToken path="/pygess/physics.py" pos="52:2:2" line-data="class World:">`World`</SwmToken> class and its methods.
3. The <SwmToken path="/pygess/physics.py" pos="22:3:3" line-data="    Initializes entity list.">`entity`</SwmToken> and <SwmToken path="/pygess/entity.py" pos="70:2:2" line-data="class MovingEntity(Entity):">`MovingEntity`</SwmToken> classes.
4. Utility functions for managing worlds and entities.
5. A test script to demonstrate usage.

# <SwmToken path="/pygess/physics.py" pos="10:2:2" line-data="class GameObjects:">`GameObjects`</SwmToken> class

The <SwmToken path="/pygess/physics.py" pos="10:2:2" line-data="class GameObjects:">`GameObjects`</SwmToken> class is responsible for storing and updating a list of entities. It acts like a sprite group but is tailored for entities.

### Initialization

<SwmSnippet path="/pygess/physics.py" line="10">

---

The constructor initializes the list of entities.

````
class GameObjects:
    '''
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
````

---

</SwmSnippet>

### Update method

<SwmSnippet path="/pygess/physics.py" line="23">

---

The <SwmToken path="/pygess/physics.py" pos="24:3:3" line-data="    ## update">`update`</SwmToken> method ensures all entities in the list are unique and calls their <SwmToken path="/pygess/physics.py" pos="24:3:3" line-data="    ## update">`update`</SwmToken> method.

````

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
    
    '''
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
````

---

</SwmSnippet>

### Append method

<SwmSnippet path="/pygess/physics.py" line="23">

---

The <SwmToken path="/pygess/physics.py" pos="46:3:3" line-data="    def append(self, *entity):">`append`</SwmToken> method adds new entities to the list.

````

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
    
    '''
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
````

---

</SwmSnippet>

# World class

The <SwmToken path="/pygess/physics.py" pos="52:2:2" line-data="class World:">`World`</SwmToken> class manages the game world, including gravity, time, and game objects.

### Initialization

<SwmSnippet path="/pygess/physics.py" line="52">

---

The constructor initializes the world with gravity, game objects, and other necessary attributes.

```
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
```

---

</SwmSnippet>

### Update method

<SwmSnippet path="/pygess/physics.py" line="78">

---

The <SwmToken path="/pygess/physics.py" pos="79:5:5" line-data="        self.runtime_obj.update()">`update`</SwmToken> method handles the world's update logic, including resetting and setting runtime states.

```

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
```

---

</SwmSnippet>

### Add and load game objects

<SwmSnippet path="/pygess/physics.py" line="78">

---

The <SwmToken path="/pygess/physics.py" pos="84:3:3" line-data="    def add_gameobj(self, *gameobj):">`add_gameobj`</SwmToken> and <SwmToken path="/pygess/physics.py" pos="88:3:3" line-data="    def load_new_object(self, *gameobj):">`load_new_object`</SwmToken> methods add game objects to the world and runtime objects, respectively.

```

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
```

---

</SwmSnippet>

### Update delta time

<SwmSnippet path="/pygess/physics.py" line="93">

---

The <SwmToken path="/pygess/physics.py" pos="92:3:3" line-data="    def update_delta_time(self):">`update_delta_time`</SwmToken> method updates the delta time for the world.

```

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
```

---

</SwmSnippet>

### Set runtime and reset methods

<SwmSnippet path="/pygess/physics.py" line="93">

---

The <SwmToken path="/pygess/physics.py" pos="101:3:3" line-data="    def __set_runtime(self):">`__set_runtime`</SwmToken> and <SwmToken path="/pygess/physics.py" pos="114:3:3" line-data="    def __reset(self):">`__reset`</SwmToken> methods manage the runtime state of the world.

```

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
```

---

</SwmSnippet>

### Deactivate method

<SwmSnippet path="/pygess/physics.py" line="122">

---

The <SwmToken path="/pygess/physics.py" pos="123:3:3" line-data="    def _deactivate(self):">`_deactivate`</SwmToken> method deactivates the world.

```

    def _deactivate(self):
        self.is_active = False
```

---

</SwmSnippet>

# Utility functions

### Get active world

<SwmSnippet path="/pygess/physics.py" line="126">

---

The <SwmToken path="/pygess/physics.py" pos="126:2:2" line-data="def get_active_world() -&gt; World:">`get_active_world`</SwmToken> function returns the currently active world.

```
def get_active_world() -> World:
    for world in worlds:
        if world.is_active:
            return world
```

---

</SwmSnippet>

### Debug no active worlds

<SwmSnippet path="/pygess/physics.py" line="131">

---

The <SwmToken path="/pygess/physics.py" pos="131:2:2" line-data="def _debug_no_active_worlds():">`_debug_no_active_worlds`</SwmToken> function counts the number of active worlds.

```
def _debug_no_active_worlds():
    counter = 0
    
    for world in worlds:
        if world.is_active:
            counter += 1
    
    return counter
```

---

</SwmSnippet>

### Set active world

<SwmSnippet path="/pygess/physics.py" line="140">

---

The <SwmToken path="/pygess/physics.py" pos="140:2:2" line-data="def set_active_world(world:World):">`set_active_world`</SwmToken> function sets a given world as active and deactivates the current active world if any.

```
def set_active_world(world:World):
    if _debug_no_active_worlds() > 0:
        get_active_world()._deactivate()
        
        
    world.is_active = True
```

---

</SwmSnippet>

### Get all worlds

<SwmSnippet path="/pygess/physics.py" line="147">

---

The <SwmToken path="/pygess/physics.py" pos="147:2:2" line-data="def get_all_worlds():">`get_all_worlds`</SwmToken> function returns all worlds.

```
def get_all_worlds():
    return worlds
```

---

</SwmSnippet>

### Update delta time for all worlds

<SwmSnippet path="/pygess/physics.py" line="150">

---

The <SwmToken path="/pygess/physics.py" pos="150:2:2" line-data="def update_delta_time():">`update_delta_time`</SwmToken> function updates the delta time for all worlds.

```
def update_delta_time():
    for w in get_all_worlds():
        w.update_delta_time()
```

---

</SwmSnippet>

### Update all worlds

<SwmSnippet path="/pygess/physics.py" line="154">

---

The <SwmToken path="/pygess/physics.py" pos="154:2:2" line-data="def update_worlds():">`update_worlds`</SwmToken> function updates all worlds.

```
def update_worlds():
    for w in get_all_worlds():
        w.update()
```

---

</SwmSnippet>

### Prefab instance functions

<SwmSnippet path="/pygess/physics.py" line="158">

---

The <SwmToken path="/pygess/physics.py" pos="158:2:2" line-data="def first_instance_of_prefab_in_world(world, prefab_entity) -&gt; &#39;entity.Entity&#39;:">`first_instance_of_prefab_in_world`</SwmToken> and <SwmToken path="/pygess/physics.py" pos="163:2:2" line-data="def all_instances_of_prefab_in_world(world, prefab_entity) -&gt; list:">`all_instances_of_prefab_in_world`</SwmToken> functions find instances of a prefab entity in a world.

```
def first_instance_of_prefab_in_world(world, prefab_entity) -> 'entity.Entity':
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            return e
```

---

</SwmSnippet>

<SwmSnippet path="/pygess/physics.py" line="163">

---

```
def all_instances_of_prefab_in_world(world, prefab_entity) -> list:
    instances = []
    for e in world.runtime_obj.entities:
        if e.parent.id == prefab_entity.id:
            instances.append(e)
    
    return instances
```

---

</SwmSnippet>

# Entity class

The <SwmToken path="/pygess/physics.py" pos="22:3:3" line-data="    Initializes entity list.">`entity`</SwmToken> class represents a game entity with position, dimensions, and optional color or image.

### Initialization

<SwmSnippet path="/pygess/entity.py" line="6">

---

The constructor initializes the entity with position, dimensions, and optional color or image.

```
class Entity(pyg.sprite.DirtySprite):
    def __init__(self, position: tuple, dimensions: tuple, color=None, image_path=None) -> None:
    
        pyg.sprite.DirtySprite.__init__(self)
        self.pos = pyg.math.Vector2(position)
        self.dimensions = dimensions
        self.color = color
        
        self.parent = None
        self.id = uuid.uuid4()
```

---

</SwmSnippet>

### Update method

<SwmSnippet path="/pygess/entity.py" line="49">

---

The <SwmToken path="/pygess/entity.py" pos="53:3:3" line-data="    def update(self):">`update`</SwmToken> method updates the entity's position, checks for collisions, and updates its sprite group.

```

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
```

---

</SwmSnippet>

### Collision methods

<SwmSnippet path="/pygess/entity.py" line="30">

---

The <SwmToken path="/pygess/entity.py" pos="35:3:3" line-data="    def update_rect(self):">`update_rect`</SwmToken>, <SwmToken path="/pygess/entity.py" pos="44:3:3" line-data="    def check_collisions(self):">`check_collisions`</SwmToken>, <SwmToken path="/pygess/entity.py" pos="47:3:3" line-data="    def is_colliding_with(self, rect):">`is_colliding_with`</SwmToken>, and <SwmToken path="/pygess/entity.py" pos="50:3:3" line-data="    def get_all_obj_colliding_with(self):">`get_all_obj_colliding_with`</SwmToken> methods handle collision detection and response.

```

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
```

---

</SwmSnippet>

# <SwmToken path="/pygess/entity.py" pos="70:2:2" line-data="class MovingEntity(Entity):">`MovingEntity`</SwmToken> class

The <SwmToken path="/pygess/entity.py" pos="70:2:2" line-data="class MovingEntity(Entity):">`MovingEntity`</SwmToken> class extends <SwmToken path="/pygess/physics.py" pos="22:3:3" line-data="    Initializes entity list.">`entity`</SwmToken> to include velocity and gravity effects.

### Initialization

<SwmSnippet path="/pygess/entity.py" line="70">

---

The constructor initializes the moving entity with position, dimensions, velocity, and optional color or image.

```
class MovingEntity(Entity):
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color:tuple=None, image_path=None) -> None:
        super().__init__(position, dimensions, color=color, image_path=image_path)
        self.velocity = pyg.math.Vector2(velocity)
        self.orignal_vel = pyg.math.Vector2(velocity)
        self.is_affected_by_gravity = False

    def update(self):
        self.active_world = physics.get_active_world()
```

---

</SwmSnippet>

### Update method

<SwmSnippet path="/pygess/entity.py" line="79">

---

The <SwmToken path="/pygess/entity.py" pos="86:5:5" line-data="            self.spr_group.update()">`update`</SwmToken> method updates the entity's position, checks for collisions, and moves the entity.

```

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
        self.pos += self.velocity * self.active_world.dt
        
        if not self.is_affected_by_gravity:
            self.velocity.y = 0
            return
        
        self.velocity += self.active_world.gravity
        
    def set_gravitified(self, bool:bool):
        self.is_affected_by_gravity = bool
```

---

</SwmSnippet>

### Move method

<SwmSnippet path="/pygess/entity.py" line="79">

---

The <SwmToken path="/pygess/entity.py" pos="82:3:3" line-data="        self.move()">`move`</SwmToken> method updates the entity's position based on its velocity and gravity.

```

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
        self.pos += self.velocity * self.active_world.dt
        
        if not self.is_affected_by_gravity:
            self.velocity.y = 0
            return
        
        self.velocity += self.active_world.gravity
        
    def set_gravitified(self, bool:bool):
        self.is_affected_by_gravity = bool
```

---

</SwmSnippet>

### Set gravity method

<SwmSnippet path="/pygess/entity.py" line="79">

---

The <SwmToken path="/pygess/entity.py" pos="102:3:3" line-data="    def set_gravitified(self, bool:bool):">`set_gravitified`</SwmToken> method enables or disables gravity for the entity.

```

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
        self.pos += self.velocity * self.active_world.dt
        
        if not self.is_affected_by_gravity:
            self.velocity.y = 0
            return
        
        self.velocity += self.active_world.gravity
        
    def set_gravitified(self, bool:bool):
        self.is_affected_by_gravity = bool
```

---

</SwmSnippet>

# Data and colors

### Data module

<SwmSnippet path="/pygess/data.py" line="1">

---

The <SwmToken path="/pygess/physics.py" pos="104:11:11" line-data="            if e.rect not in data.all_rects:">`data`</SwmToken> module contains a list of all rectangles for collision detection.

```
all_rects = []
```

---

</SwmSnippet>

### Colors module

<SwmSnippet path="/pygess/colors.py" line="1">

---

The <SwmToken path="/pygess/__init__.py" pos="3:6:6" line-data="from . import colors">`colors`</SwmToken> module defines some basic colors.

```
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```

---

</SwmSnippet>

# Initialization

### Init module

<SwmSnippet path="/pygess/__init__.py" line="1">

---

The <SwmToken path="/pygess/physics.py" pos="19:3:3" line-data="    def __init__(self, entities:list) -&gt; None:">`__init__`</SwmToken> module imports necessary components and sets the version.

```
from . import entity
from . import data
from . import colors
from . import physics
from . import entity
import time


__version__ = '1.0.1'
```

---

</SwmSnippet>

# Test script

Here is a test script to demonstrate the usage of PyGess:

```python
import pygess
import time

# Create entities
entity1 = pygess.entity.Entity((50, 50), (10, 10), color=pygess.colors.RED)
entity2 = pygess.entity.MovingEntity((100, 100), (10, 10), (1, 1), color=pygess.colors.BLUE)

# Create a world with gravity
world = pygess.physics.World((0, 9.8), entity1, entity2)

# Set the world as active
pygess.physics.set_active_world(world)

# Main loop
while True:
    pygess.physics.update_worlds()
    time.sleep(0.016)  # Simulate 60 FPS
```

This script creates a world with two entities, sets the world as active, and continuously updates the world in a loop.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBcHlnZXNzLWZvcmslM0ElM0FNYW5nby1DcmVhdG9ycw==" repo-name="pygess-fork"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
