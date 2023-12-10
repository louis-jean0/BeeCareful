class CarnivorousPlant():
    
    def __init__(self,position,zone):
        self.zone = zone
        self.position = position
        self.nb_bees_eaten = 0
        self.isEating = False
        self.cooldown = 1000
        self.time = 0

    def eat_bee(self,bee):
        for bee in self.zone.beeList:
            bee.nbCarniPlantes.add(tuple(self.position))
            bee.set_alerte(True)
        self.isEating = True
        bee.die()
        
    def draw_carni_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] 
        y = position[1]  
        window.blit(image, (x, y))

    def get_position(self):
        return self.position

    def get_isEating(self):
        return self.isEating

    def update(self):
        if(self.isEating):
            if self.time >= self.cooldown:
                self.isEating = False
                self.time = 0
            else:
                self.time += 1