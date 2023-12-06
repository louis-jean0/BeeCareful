import pygame

from Zone import *

class Map:

    def __init__(self, grid_width, grid_height, zone_width, zone_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.zones = [[Zone(zone_width,zone_height,x,y) for x in range(grid_width)] for y in range(grid_height)]

    def populate_map(self, max_plants_per_zone, max_carnivorous_plants_per_zone):
        for row in self.zones:
            for zone in row:
                num_plants = 10#random.randint(0, max_plants_per_zone)
                num_carnivorous_plants = random.randint(0, max_carnivorous_plants_per_zone)
                zone.populate_zone(num_plants, num_carnivorous_plants)

    def draw(self, window):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * self.zone_width, y * self.zone_height, self.zone_width, self.zone_height)
                pygame.draw.rect(window, (255, 255, 255), rect, 1)  # Dessiner les bordures de chaque zone
