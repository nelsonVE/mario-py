import pygame
from collisions import Collision


class Entity:
    class Meta:
        abstract = True

    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    def __init__(self, x, y, screen, world):
        self.animation = 0
        self.counter = 0
        self.image = None
        self.rect = None
        self.screen = screen
        self.vel_y = 0
        self.jumping = False
        self.old_direction = None
        self.dx = 0
        self.dy = 0
        self.world = world
        self.collision = Collision()
        self.sprite = pygame.sprite.Sprite()
        self.direction = None

    def generate_sprite(self):
        self.sprite.image = self.image
        self.sprite.rect = self.rect
        self.sprite.rect.x = self.rect.x
        self.sprite.rect.y = self.rect.y
