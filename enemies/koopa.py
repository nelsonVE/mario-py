from entity import Entity
import tiles
import pygame
import constants


enemy_sprites = {
    0: ((1, 1), (16, 27)),
    1: ((2, 1), (16, 27)),
}


class Koopa(Entity):
    VELOCITY_X = 2

    def __init__(self, x, y, screen, world, player):
        super().__init__(x, y, screen, world)
        self.images_left = [pygame.image.frombuffer(*tiles.get_tile(3, *enemy_sprites.get(index)[0], *enemy_sprites.get(index)[1])) for index in range(0, 2)]
        self.images_right = [pygame.transform.flip(image, True, False) for image in self.images_left]
        self.image = pygame.transform.scale(self.images_right[self.animation], enemy_sprites.get(self.animation)[1])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.falling = False
        self.direction = self.DIRECTION_RIGHT
        self.player = player

    def update(self):
        self.dx = 0
        self.dy = 0
        self.counter += 1
        actual_width = self.image.get_width()
        actual_height = self.image.get_height()
        self.generate_sprite()
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.bottom > constants.HEIGHT:
            self.rect.bottom = constants.HEIGHT
            self.dy = 0
        
        self.vel_y += 1 if self.vel_y < 10 else 0

        self.dy += self.vel_y

        if self.vel_y > 0 and not self.jumping:
            self.falling = True

        if self.direction == self.DIRECTION_RIGHT:
            self.dx += self.get_vel_x()

            if self.counter >= 8:
                self.animation = 0 if self.animation == 1 else 1
                self.image = pygame.transform.scale(self.images_right[self.animation], enemy_sprites.get(self.animation)[1])
                self.counter = 0
        elif self.direction == self.DIRECTION_LEFT:
            self.dx -= 2 if not self.world.is_moving() else 6

            if self.counter >= 8:
                self.animation = 0 if self.animation == 1 else 1
                self.image = pygame.transform.scale(self.images_left[self.animation], enemy_sprites.get(self.animation)[1])
                self.counter = 0

        self.collision.enemy(self, self.player, self.world)

        self.rect.x += self.dx
        self.rect.y += self.dy

        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
