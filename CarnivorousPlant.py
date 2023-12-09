class CarnivorousPlant():
    
    def __init__(self,position):
        self.position = position
        self.nb_bees_eaten = 0
        self.isEating = False

    def eat_bee(self,bee):
        bee.die()
        self.isEating = True
        
    def draw_carni_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] 
        y = position[1]  
        window.blit(image, (x, y))

    def get_position(self):
        return self.position

    def get_isEating(self):
        return self.isEating