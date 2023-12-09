import random
from Plant import Plant
from CarnivorousPlant import CarnivorousPlant

class Zone:
    def __init__(self,width,height,x,y):
        self.zone_id = (x,y)
        self.minX = width * x
        self.maxX = (width * (x+1))-1
        self.minY = height * y
        self.maxY = (height * (y+1))-1
        self.width = width
        self.height = height
        self.plants = []
        self.carnivorous_plants = []
        self.has_carnivorous_plant = False
        self.nbPlante = 0

    def populate_zone(self, num_plants, num_carnivorous_plants):
        nbPlante = num_plants + num_carnivorous_plants
        max_pollen = 10
        cooldown = 5
        for i in range(num_plants):
            self.plants.append(Plant([random.randint(self.minX,self.maxX),random.randint(self.minY,self.maxY)],max_pollen,cooldown) )
        self.carnivorous_plants = [CarnivorousPlant(2) for _ in range(num_carnivorous_plants)]
        self.has_carnivorous_plant = num_carnivorous_plants > 0

    def getMinX():
        return minX

    def getMaxX():
        return maxX

    def getMinY():
        return minY

    def getMaxY():
        return maxY