import random

class Bee:
    def __init__(self, grid_position, pixel_position, home_position):
        self.grid_position = grid_position  # Position actuelle de l'abeille
        self.pixel_position = pixel_position
        self.home_position = home_position  # Position de la ruche
        self.pollen_capacity = 10  # Capacité maximale de pollen que l'abeille peut transporter
        self.pollen_collected = 0  # Quantité de pollen actuellement collectée
        self.target_position = None
    
    def set_target(self, target_position_in_grid, zone_width, zone_height):
        self.target_position = [target_position_in_grid[0] * zone_width,target_position_in_grid[1] * zone_height]

    def move(self, new_position):
        # Mettre à jour la position de l'abeille
        self.pixel_position = new_position

    def collect_pollen(self, plant):
        # Collecter du pollen d'une plante
        if self.pollen_collected < self.pollen_capacity and plant.current_pollen > 0:
            pollen_to_collect = min(plant.current_pollen, self.pollen_capacity - self.pollen_collected)
            self.pollen_collected += pollen_to_collect
            plant.current_pollen -= pollen_to_collect

    def return_to_hive(self):
        # Retourner à la ruche pour déposer le pollen
        if self.position != self.home_position:
            self.move(self.home_position)
        # Déposer le pollen à la ruche et réinitialiser le compteur de pollen
        self.deposit_pollen()

    def deposit_pollen(self):
        # Déposer le pollen à la ruche
        # Cela pourrait impliquer d'augmenter un compteur dans la ruche ou une autre logique
        self.pollen_collected = 0

    def communicate_flower_location(self, flower_location):
        # Communiquer l'emplacement d'une fleur à d'autres abeilles
        # Cela pourrait impliquer de mettre à jour une sorte de mémoire partagée ou de carte
        pass

    def update(self):
        # Mettre à jour le comportement de l'abeille à chaque tick du jeu
        # Implémenter la logique de décision pour se déplacer, récolter du pollen, etc.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.move(random.choice(directions))
        pass

    def draw_bee(self, window, cell_width, cell_height, image):
        x = self.pixel_position[0]
        y = self.pixel_position[1] 
        window.blit(image, (x, y))
