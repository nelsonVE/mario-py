import pygame
from pygame.locals import *

import constants
import level_data
from world import World
from player import Player
from collisions import Collision
from enemies.koopa import Koopa

pygame.init()

clock = pygame.time.Clock()
fps = 60

width = constants.WIDTH
height = constants.HEIGHT

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Super Mario Python')

run = True
tile_size = 32

world = World(level_data.basic, screen)
player = Player(1, 1, screen, world)
enemy = Koopa(7 * constants.TILE_SIZE, 9 * constants.TILE_SIZE, screen, world, player)
collision = Collision()

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, height))

while run:
    clock.tick(fps)
    screen.fill((102, 204, 255))

    #draw_grid()

    world.draw()
    player.update()
    enemy.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()