import tiles
import pygame
import level_data
import constants

class World():
    def __init__(self, data, screen):
        self.tile_list = []
        self.screen = screen
        row_count = 0
        self.sprite_group = pygame.sprite.Group()
        self.move = False

        for row in data:
            col_count = 0

            for tile in row:
                if level_data.tile_textures.get(tile):
                    sprite = pygame.sprite.Sprite()
                    x, y = level_data.tile_textures.get(tile)
                    texture = pygame.image.frombuffer(*tiles.get_tile(1, x, y))
                    image = pygame.transform.scale(texture, (constants.TILE_SIZE, constants.TILE_SIZE))
                    image_rect = image.get_rect()
                    sprite.image = image
                    sprite.rect = image_rect
                    sprite.rect.x = col_count * constants.TILE_SIZE
                    sprite.rect.y = row_count * constants.TILE_SIZE
                    image_rect.x = col_count * constants.TILE_SIZE
                    image_rect.y = row_count * constants.TILE_SIZE
                    tile = (image, image_rect)

                    self.sprite_group.add(sprite)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        if self.move:
            for spr in self.sprite_group:
                spr.rect.move_ip(-6, 0)

        pygame.sprite.Group.draw(self.sprite_group, self.screen)

    def move_world(self, move):
        self.move = move

    def is_moving(self):
        print('moving: ', self.move)
        return self.move
