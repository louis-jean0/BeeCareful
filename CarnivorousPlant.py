from Plant import Plant

class CarnivorousPlant():
    
    def __init__(self,position,range):
        self.position = position
        self.nb_bees_eaten = 0
        self.range = range

    def draw_carnivorous_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] * cell_width
        y = position[1] * cell_height
        window.blit(image, (x, y))