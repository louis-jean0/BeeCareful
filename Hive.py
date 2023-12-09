import random
import math
from Map import Map

class Hive:
    
    def __init__(self, position,grid_width, grid_height, zone_width, zone_height):
        self.position = position  # Position de la ruche sur la grille
        self.stored_pollen = 0  # Quantité actuelle de pollen stocké
        self.shared_memory = []
        self.bee_waiting_list = []  # Liste d'abeilles en attente d'instructions
        self.zone_tier_list = []    # Liste de priorité des zones
        self.bee_zone_list = []     # Liste de tuple (bee,zone,time) associant une abeille, sa zone ainsi que le temps qu'elle met, incrémenter dans updates()
        self.hive_map = Map(grid_width, grid_height, zone_width, zone_height)

    def add_to_bee_waiting_list_init(self,bee):
        self.bee_waiting_list.append(bee)

    def update(self):
        # Mettre à jour la ruche à chaque tick du jeu
        # Cela pourrait inclure des actions comme la production de nouvelles abeilles
        
        pass
        
    def store_pollen_from_bee(self, amount):
        # Ajouter du pollen au stockage, sans dépasser la capacité
        self.stored_pollen += amount

    def wait_order(self,bee):
        # Fonction appelé par une abeille lorsqu'elle attend une action
        self.bee_waiting_list.append(bee)
        
    def give_action(self):
        # Donne une action à la 1ère abeille dans la liste
        if self.bee_waiting_list:
            current_bee = self.bee_waiting_list[0]
            
            
            
            current_bee.set_target(self.zone_tier_list[0].random_position())
            self.zone_tier_list[0].nbPlanteCooldown += 1
            self.score(self.zone_tier_list[0])
            self.sort_priority()
            self.bee_waiting_list.pop(0)
            
            
    def sort_priority(self):
        self.zone_tier_list = []
        zone_liste = []
        for row in self.hive_map.zones:
            for zone in row:
                zone_liste.append(zone)
        
        for z in zone_liste:
            if self.zone_tier_list == []:
                self.zone_tier_list.append(z)
            else:
                for i in range(len(self.zone_tier_list)):
                    if z.score > self.zone_tier_list[i].score:
                        self.zone_tier_list.insert(i,z)
                        break
    
    def print_priority(self):
        for zone in self.zone_tier_list :
            print(zone.zone_id)
    def score_init(self):
        for row in self.hive_map.zones:
            for zone in row:
                self.score(zone)
    
    def score(self,zone):    
    # score d'une zone = distance + nbPlantes - nbPlante Carnivore Connu - nbPlante en Cooldown
        if self.position[0] == zone.zone_id[0] and self.position[1] == zone.zone_id[1]:
            distance = 1.01
        else:
            distance = 1 / math.sqrt(pow((self.position[0] - zone.zone_id[0]),2) + pow((self.position[1] - zone.zone_id[1]),2))
        if zone.nbPlante == 0:
            zone.score = 0
        else:    
            zone.score = (distance + zone.nbPlante - zone.nbCarniPlante - zone.nbPlanteCooldown) * (zone.nbPlante - zone.nbCarniPlante / zone.nbPlante)
                
                
    
    # nbPlante Carnivore Connu : comment reconnaitre une plante carnivore ?
    # nbPlante en Cooldown donné par les abeilles, en analysant la zone, elles connaissent le nombre de fleurs occupés
            
     
    def draw_hive(self, window, position, zone_width, zone_height, image):
        x = position[0] * zone_width
        y = position[1] * zone_height
        window.blit(image,(x,y))