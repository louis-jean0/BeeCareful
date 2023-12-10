import random

class Plant:
    
    def __init__(self,position,max_pollen,cooldown):
        
        self.position = position
        self.max_pollen = max_pollen
        self.current_pollen = max_pollen
        self.cooldown = cooldown
        self.timer = cooldown
        self.onCooldown = False

    def draw_plant(self, window, position, cell_width, cell_height, image):
        x = position[0] 
        y = position[1]  
        window.blit(image, (x, y))

    def get_pollen(self):
        speed = 1 # vitesse a laquelle le pollen est recupere
        self.current_pollen -= speed
        if self.current_pollen <= 0:
            self.onCooldown = True
        return speed # retourne le pollen pris

    def restaure(self):
        speed = 1 # vitesse a laquelle le pollen est restaure
        self.current_pollen += speed
        if self.current_pollen >= self.max_pollen:
            self.current_pollen = max_pollen
            self.onCooldown = False

    def isOnCD(self):
        return self.onCooldown

    def get_position(self):
        return self.position