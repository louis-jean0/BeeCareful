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
        print("\n",self.zone_id," : ",num_plants)
        for i in range(num_plants):
            rand = random.randint(0,100)
            positionRandom = []
            good_position = False
            ecartPlante = 40
            while(not(good_position)):
                good_position = True
                positionRandom = [random.randint(self.minX,self.maxX-50),random.randint(self.minY,self.maxY-50)]
                for plant in self.plants:
                    if plant.position[0] < positionRandom[0] and  positionRandom[0] < plant.position[0]+ecartPlante or plant.position[1] < positionRandom[1] and  positionRandom[1] < plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if plant.position[0] < positionRandom[0] and  positionRandom[0] < plant.position[0]+ecartPlante or plant.position[1] < positionRandom[1]+ecartPlante and  positionRandom[1]+ecartPlante < plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if plant.position[0] < positionRandom[0]+ecartPlante and  positionRandom[0]+ecartPlante < plant.position[0]+ecartPlante or plant.position[1] < positionRandom[1] and  positionRandom[1] < plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if plant.position[0] < positionRandom[0]+ecartPlante and  positionRandom[0]+ecartPlante < plant.position[0]+ecartPlante or plant.position[1] < positionRandom[1]+ecartPlante and  positionRandom[1]+ecartPlante < plant.position[1]+ecartPlante:
                        
                        good_position = False
                for carni_plant in self.carnivorous_plants:
                    if carni_plant.position[0] < positionRandom[0] and  positionRandom[0] < carni_plant.position[0]+ecartPlante and carni_plant.position[1] < positionRandom[1] and  positionRandom[1] < carni_plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if carni_plant.position[0] < positionRandom[0] and  positionRandom[0] < carni_plant.position[0]+ecartPlante and carni_plant.position[1] < positionRandom[1]+ecartPlante and  positionRandom[1]+ecartPlante < carni_plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if carni_plant.position[0] < positionRandom[0]+ecartPlante and  positionRandom[0]+ecartPlante < carni_plant.position[0]+ecartPlante and carni_plant.position[1] < positionRandom[1] and  positionRandom[1] < carni_plant.position[1]+ecartPlante:
                        
                        good_position = False
                    if carni_plant.position[0] < positionRandom[0]+ecartPlante and  positionRandom[0]+ecartPlante < carni_plant.position[0]+ecartPlante and carni_plant.position[1]+ecartPlante < positionRandom[1]+ecartPlante and  positionRandom[1] < carni_plant.position[1]+ecartPlante:
                      
                        good_position = False
            
            
            if rand < 20:
                self.carnivorous_plants.append(CarnivorousPlant(positionRandom) )
            else:
                self.plants.append(Plant(positionRandom,max_pollen,cooldown) )
        
        self.has_carnivorous_plant = len(self.carnivorous_plants) > 0

    def getMinX():
        return minX

    def getMaxX():
        return maxX

    def getMinY():
        return minY

    def getMaxY():
        return maxY