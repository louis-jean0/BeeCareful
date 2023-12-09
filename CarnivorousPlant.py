class CarnivorousPlant():
    
    def __init__(self,position):
        self.position = position
        self.nb_bees_eaten = 0

    def eat_bee(self,bee):
        
        pass
        
    def draw_carni_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] 
        y = position[1]  
        window.blit(image, (x, y))