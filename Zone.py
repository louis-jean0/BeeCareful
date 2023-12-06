import random
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
        position = [random.randint(0,self.width - 1),random.randint(0,self.height - 1)]
        cooldown = 5
        self.plants = [Plant(position,max_pollen,cooldown) for _ in range(num_plants)]
        self.carnivorous_plants = [CarnivorousPlant(2) for _ in range(num_carnivorous_plants)]
        self.has_carnivorous_plant = num_carnivorous_plants > 0
