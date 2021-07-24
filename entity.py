import pygame
from collisions import Collision


class Entity:
    class Meta:
        abstract = True

    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'
    VELOCITY_X = 4

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

    def get_vel_x(self):
        velocity = self.VELOCITY_X
        if self.world.is_moving():
            velocity = 0
        return velocity

    def get_dx(self):
        velocity = self.VELOCITY_X

        if self.dx < 0 and not self.world.is_moving():
            velocity *= -1

        return velocity
