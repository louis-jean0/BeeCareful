class Plant:
    
    def __init__(self,position,max_pollen,cooldown):
        self.position = position
        self.max_pollen = max_pollen
        self.current_pollen = max_pollen
        self.cooldown = cooldown
        self.timer = cooldown

    def draw_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] * cell_width
        y = position[1] * cell_height
        window.blit(image, (x, y))
