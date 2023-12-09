import random
from utils import *
from Plant import Plant
from CarnivorousPlant import CarnivorousPlant

class Zone:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.plants = []
        self.carnivorous_plants = []
        self.has_carnivorous_plant = False

    def populate_zone(self, num_plants, num_carnivorous_plants):
        max_pollen = 10
        plant_position = [random.randint(0,self.width - 1),random.randint(0,self.height - 1)]
        carnivorous_plant_position = [random.randint(0,self.width - 1),random.randint(0,self.height - 1)]
        plant_position = grid_to_pixel(plant_position,self.width,self.height)
        carnivorous_plant_position = grid_to_pixel(carnivorous_plant_position,self.width,self.height)
        cooldown = 5
        self.plants = [Plant(plant_position,max_pollen,cooldown) for _ in range(num_plants)]
        self.carnivorous_plants = [CarnivorousPlant(carnivorous_plant_position,2) for _ in range(num_carnivorous_plants)]
        self.has_carnivorous_plant = num_carnivorous_plants > 0
