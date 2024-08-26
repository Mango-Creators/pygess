import pygame as pyg
from ..entity import MovingEntity
from .. import data
from .. import physics

class Enemy(MovingEntity):
    def __init__(self, position: tuple, dimensions: tuple, velocity: tuple, color=None, image_path=None, attack_range: float = 50.0) -> None:
        MovingEntity.__init__(self, position, dimensions, velocity, color, image_path)
        self.attack_range = attack_range
        self.player = None
        self.attack_mode = None  # defined by usr

    def set_player(self, player):
        self.player = player

    def set_attack_mode(self, attack_function):
        self.attack_mode = attack_function

    def move_towards(self):
        if self.player:
            direction = self.player.pos - self.pos
            distance = direction.length()
            if distance <= self.attack_range:
                if self.attack_mode:
                    self.attack_mode(self)
            else:
                direction.normalize_ip()
                self.pos += direction * self.velocity * physics.Dt

    def update(self):
        self.move_towards()
        self.update_rect()
        self.check_collisions()
        if self in self.spr_group:
            self.spr_group.update()
        self.spr_group.draw(pyg.display.get_surface())
