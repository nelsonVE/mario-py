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
        for tile in self.tile_list:
            self.screen.blit(*tile)
            pygame.draw.rect(self.screen, (0, 255, 0), tile[1], 2)
