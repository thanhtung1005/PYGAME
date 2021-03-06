import pygame
import setting
import platforms
import monsters
import items

def load_file(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    return data

def load_ground(filename):
    data = load_file(filename)
    ground = []
    for tile in data:
        ground.append(list(tile))
    return ground

def load_enemies(filename):
    data = load_file(filename)
    enemies = []
    for enemy in data:
        enemies.append(enemy.split(' '))
    return enemies

class Map(pygame.sprite.Sprite):
    """ This is a generic super-class used to define a map.
        Create a child class for each map with map-specific info."""

    # Lists of sprites used in all maps
    platform_list = None
    enemy_list = None
    item_list = None

    # Background map
    background = None
    ground = None

    # How far this map been scrolled
    map_scroll = 0
    map_limit = 0

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        """ Update everything on this map"""
        self.enemy_list.update(self.platform_list)
        self.item_list.update()

        # Find all enemy collide with the player
        hits = pygame.sprite.spritecollide(self.player, self.enemy_list,
                                           False, pygame.sprite.collide_rect_ratio(0.7))
        for enemy in hits:
            if enemy.rect.x >= self.player.rect.x:
                if not enemy.face_right:
                    enemy.attacking = True
            else:
                if enemy.face_right:
                    enemy.attacking = True
            if enemy.image in enemy.true_attack:
                self.player.beaten = True
                self.player.current_HP -= enemy.damage / 5
            if self.player.image in self.player.true_attack:
                if (self.player.rect.x <= enemy.rect.x and self.player.face_right) or \
                    (self.player.rect.x > enemy.rect.x and  not self.player.face_right):
                    enemy.beaten = True
                    enemy.current_HP -= self.player.damage / 5
    def draw(self, screen):
        """ Draw everything on this map"""

        # Draw background
        screen.blit(self.background, (0, 0))
        # Draw all platform
        screen.blit(self.ground, (self.map_scroll, 0))

        # Draw all enemmy
        for enemy in self.enemy_list:
            enemy.draw(screen)
        # Draw all item
        self.item_list.draw(screen)

    def scroll_map(self, scroll_x):
        """ When the user moves left/right and we need to scroll everything"""

        self.map_scroll += scroll_x

        for platform in self.platform_list:
            platform.rect.x += scroll_x

        for enemy in self.enemy_list:
            enemy.rect.x += scroll_x

class Map_01(Map):
    """ Create map 1. """
    def __init__(self, player):
        # Call the parent constructor
        super().__init__(player)

        self.background = pygame.image.load('image/Map_1/background.png').convert()
        self.ground = pygame.image.load('image/Map_1/front_map.png').convert_alpha()
        self.ground.set_colorkey(setting.WHITE)
        tiles = load_ground('image/Map_1/map.txt')
        self.map_limit = setting.TILE_SIZE * len(tiles[0])
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                if tiles[x][y] != '0':
                    tile = platforms.Platform(y * setting.TILE_SIZE, x * setting.TILE_SIZE)
                    self.platform_list.add(tile)
        enemies = load_enemies('image/Map_1/enemies.txt')
        for enemy in enemies:
            if enemy[0] == 'Wolf':
                self.enemy_list.add(monsters.Wolf(int(enemy[1]), int(enemy[2])))
            elif enemy[0] == 'Female_Zombie':
                self.enemy_list.add(monsters.Female_Zombie(int(enemy[1]), int(enemy[2])))
            else:
                self.enemy_list.add(monsters.Male_Zombie(int(enemy[1]), int(enemy[2])))
class Map_02(Map):
    " Create map 2. "
    def __init__(self, player):
        # Call the parent constructor
        super().__init__(player)

        self.background = pygame.image.load('image/Map_2/map.png').convert()
        self.ground = pygame.image.load('image/Map_2/map.png').convert_alpha()
        tiles = load_ground('image/Map_2/map.txt')
        self.map_limit = setting.TILE_SIZE * len(tiles[0])
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                if tiles[x][y] != '0':
                    tile = platforms.Platform(y * setting.TILE_SIZE, x * setting.TILE_SIZE)
                    self.platform_list.add(tile)
        enemies = load_enemies('image/Map_2/enemies.txt')
        for enemy in enemies:
            if enemy[0] == 'Wolf':
                self.enemy_list.add(monsters.Wolf(int(enemy[1]), int(enemy[2])))
            elif enemy[0] == 'Female_Zombie':
                self.enemy_list.add(monsters.Female_Zombie(int(enemy[1]), int(enemy[2])))
            else:
                self.enemy_list.add(monsters.Male_Zombie(int(enemy[1]), int(enemy[2])))
class Map_03(Map):
    " Create map 3. "
    def __init__(self, player):
        # Call the parent constructor
        super().__init__(player)

        self.background = pygame.image.load('image/Map_3/map.png').convert()
        self.ground = pygame.image.load('image/Map_3/map.png').convert_alpha()
        tiles = load_ground('image/Map_3/map.txt')
        self.map_limit = setting.TILE_SIZE * len(tiles[0])
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                if tiles[x][y] != '0':
                    tile = platforms.Platform(y * setting.TILE_SIZE, x * setting.TILE_SIZE)
                    self.platform_list.add(tile)
        enemies = load_enemies('image/Map_3/enemies.txt')
        for enemy in enemies:
            if enemy[0] == 'Wolf':
                self.enemy_list.add(monsters.Wolf(int(enemy[1]), int(enemy[2])))
            elif enemy[0] == 'Female_Zombie':
                self.enemy_list.add(monsters.Female_Zombie(int(enemy[1]), int(enemy[2])))
            else:
                self.enemy_list.add(monsters.Male_Zombie(int(enemy[1]), int(enemy[2])))
class Map_04(Map):
    " Create map 4. "
    def __init__(self, player):
        # Call the parent constructor
        super().__init__(player)

        self.background = pygame.image.load('image/Map_4/map.png').convert()
        self.ground = pygame.image.load('image/Map_4/map.png').convert_alpha()
        tiles = load_ground('image/Map_4/map.txt')
        self.map_limit = setting.TILE_SIZE * len(tiles[0])
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                if tiles[x][y] != '0':
                    tile = platforms.Platform(y * setting.TILE_SIZE, x * setting.TILE_SIZE)
                    self.platform_list.add(tile)
        enemies = load_enemies('image/Map_4/enemies.txt')
        for enemy in enemies:
            if enemy[0] == 'Wolf':
                self.enemy_list.add(monsters.Wolf(int(enemy[1]), int(enemy[2])))
            elif enemy[0] == 'Female_Zombie':
                self.enemy_list.add(monsters.Female_Zombie(int(enemy[1]), int(enemy[2])))
            else:
                self.enemy_list.add(monsters.Male_Zombie(int(enemy[1]), int(enemy[2])))