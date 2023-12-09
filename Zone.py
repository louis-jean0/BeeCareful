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
            rand = random.randint(0,100)
            if rand < 20:
                self.carnivorous_plants.append(CarnivorousPlant([random.randint(self.minX+5,self.maxX-5),random.randint(self.minY+2,self.maxY)-2]) )
            else:
                self.plants.append(Plant([random.randint(self.minX+5,self.maxX-5),random.randint(self.minY+2,self.maxY)-2],max_pollen,cooldown) )
        
        self.has_carnivorous_plant = len(self.carnivorous_plants) > 0

    def getMinX(self):
        return self.minX

    def getMaxX(self):
        return self.maxX

    def getMinY(self):
        return self.minY

    def getMaxY(self):
        return self.maxY