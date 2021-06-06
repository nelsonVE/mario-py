import pygame
import tiles
import constants
from entity import Entity

player_tiles = {
    0: ((1, 1), (14, 20)),
    1: ((2, 1), (14, 20)),
    2: ((3, 1), (14, 20)),
    3: ((3, 1), (14, 20)),
}

class Player(Entity):
    def __init__(self, x, y, screen, world):
        super().__init__(x, y, screen, world)
        self.images_left = [pygame.image.frombuffer(*tiles.get_tile(2, *player_tiles.get(index)[0], *player_tiles.get(index)[1])) for index in range(0, 2)]
        self.images_right = [pygame.transform.flip(image, True, False) for image in self.images_left]
        self.images_death = [pygame.image.frombuffer(*tiles.get_tile(2, *player_tiles.get(index)[0], *player_tiles.get(index)[1])) for index in (2, 3)]
        self.image = pygame.transform.scale(self.images_right[self.animation], player_tiles.get(self.animation)[1])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.falling = False
        self.alive = True
        self.dying = False

    def update(self):
        key = pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0
        self.counter += 1
        actual_width = self.image.get_width()
        actual_height = self.image.get_height()
        self.generate_sprite()
        self.mask = pygame.mask.from_surface(self.image)

        if not self.alive:
            self.animation = 0 if self.animation == 1 else 1
            if not self.dying:
                self.vel_y = -15
            self.image = pygame.transform.scale(self.images_death[self.animation], player_tiles.get(self.animation)[1])
            self.dy += self.vel_y
            self.dying = True
        else:
            if key[pygame.K_a]:
                self.dx -= 4
                self.old_direction = pygame.K_a
                if self.counter >= 8:
                    self.animation = 0 if self.animation == 1 else 1
                    self.image = pygame.transform.scale(self.images_left[self.animation], player_tiles.get(self.animation)[1])
                    self.counter = 0

            if key[pygame.K_d]:
                self.dx += 4
                self.old_direction = pygame.K_d
                if self.counter >= 8:
                    self.animation = 0 if self.animation == 1 else 1
                    self.image = pygame.transform.scale(self.images_right[self.animation], player_tiles.get(self.animation)[1])
                    self.counter = 0

            if key[pygame.K_SPACE] and not(self.jumping or self.falling):
                self.vel_y = -15
                self.jumping = True

            if self.rect.bottom > constants.HEIGHT:
                self.rect.bottom = constants.HEIGHT
                self.dy = 0

            self.dy += self.vel_y

            if self.vel_y > 0 and not self.jumping:
                self.falling = True

            if self.dx == 0:
                self.animation = 0
                if self.old_direction == pygame.K_d:
                    self.image = pygame.transform.scale(self.images_right[self.animation], player_tiles.get(self.animation)[1])
                elif self.old_direction == pygame.K_a:
                    self.image = pygame.transform.scale(self.images_left[self.animation], player_tiles.get(self.animation)[1])

            self.collision.detect(self, self.world)
        self.vel_y += 1 if self.vel_y < 10 else 0
        self.rect.x += self.dx
        self.rect.y += self.dy

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
