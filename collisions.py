class Collision:
    def detect(self, player, world):
        player_width = player.image.get_width()
        player_height = player.image.get_height()

        for tile in world.tile_list:
            if tile[1].colliderect(player.rect.x, player.rect.y + player.dy, player_width, player_height):
                if player.vel_y < 0:
                    player.dy = tile[1].bottom - player.rect.top
                    player.vel_y = 0
                elif player.vel_y >= 0:
                    player.dy = tile[1].top - player.rect.bottom
                    player.vel_y = 0
                    player.jumping = False
                    player.falling = False

            if tile[1].colliderect(player.rect.x + player.dx, player.rect.y, player_width, player_height):
                player.dx = 0

    def enemy(self, enemy, player, world):
        enemy_width = enemy.image.get_width()
        enemy_height = enemy.image.get_height()

        for tile in world.tile_list:
            if tile[1].colliderect(enemy.rect.x, enemy.rect.y + enemy.dy, enemy_width, enemy_height):
                if enemy.vel_y < 0:
                    enemy.dy = tile[1].bottom - enemy.rect.top
                    enemy.vel_y = 0
                elif enemy.vel_y >= 0:
                    enemy.dy = tile[1].top - enemy.rect.bottom
                    enemy.vel_y = 0

            if tile[1].colliderect(enemy.rect.x + enemy.dx, enemy.rect.y, enemy_width, enemy_height):
                enemy.direction = enemy.DIRECTION_RIGHT if enemy.direction == enemy.DIRECTION_LEFT else enemy.DIRECTION_LEFT
                enemy.dx = 0

        if player.rect.colliderect(enemy.rect.x + enemy.dx, enemy.rect.y, enemy_width, enemy_height):
            player.alive = False