import random
import pygame

from Hive import Hive
from utils import *
from Map import Map
from utils import *
from CarnivorousPlant import CarnivorousPlant
from Plant import Plant

class Bee:
    def __init__(self, map, grid_position, pixel_position, home_position,hive):
        self.map = map
        self.grid_position = grid_position  # Position actuelle de l'abeille
        self.pixel_position = pixel_position
        self.home_position = home_position  # Position de la ruche
        self.pollen_capacity = 500 # Capacité maximale de pollen que l'abeille peut transporter
        self.pollen_collected = 0 # Quantité de pollen actuellement collectée
        self.target_position = None
        self.hive = hive
        self.go_store = True
        self.direction = False
        self.is_alive = True
        self.zone_targeted = None
        self.InZoneTargeted = False
        self.notDeposedYet = False
        #Paramètres à transmettre à la ruche
        self.nbPlantes = 0
        self.nbCarniPlantes = set()
        self.nbPlantesOccupee = 0
        self.enAlerte = False

    def set_target(self, target_position):
        self.target_position = target_position
        
    def send_to_target(self,zone,target_position):
        self.set_target(target_position)
        self.zone_targeted = zone

    def get_hive(self):
        return self.hive.getNumero()

    def move(self, new_position):
        # Mettre à jour la position de l'abeille
        self.pixel_position = new_position

    def set_alerte(self,val):
        self.enAlerte = val

    def isEnAlerte(self):
        return self.enAlerte

    def move_towards_target(self):
        if self.target_position:
            # Calculer le vecteur de direction vers la cible
            direction = (self.target_position[0] - self.pixel_position[0], self.target_position[1] - self.pixel_position[1])
            distance = (direction[0]**2 + direction[1]**2)**0.5

            if direction[0] <= 0:
                self.direction = False
            else:
                self.direction = True


            # Normaliser le vecteur de direction
            if distance > 0:
                direction = (direction[0] / distance, direction[1] / distance)

            # Déplacer l'abeille vers la cible
            self.pixel_position = (self.pixel_position[0] + direction[0] * 2, 
                             self.pixel_position[1] + direction[1] * 2)

            # Vérifier si l'abeille a atteint la cible (ou est suffisamment proche)
            if distance < 0.5:
                self.position = self.target_position
                self.target_position = None
            
            self.grid_position = pixel_to_grid(self.pixel_position,self.map.zone_width,self.map.zone_height)

    def collect_pollen(self, plant):
        # Collecter du pollen d'une plante
        if self.pollen_collected < self.pollen_capacity and plant.current_pollen > 0:
            pollen_to_collect = min(plant.current_pollen, self.pollen_capacity - self.pollen_collected)
            self.pollen_collected += pollen_to_collect
            plant.current_pollen -= pollen_to_collect
        if self.pollen_collected == self.pollen_capacity:
            self.return_to_hive()

    def return_to_hive(self):
        # Retourner à la ruche pour déposer le pollen
        
        if not(self.isAtHive()):
            self.set_target(self.home_position)
            self.move_towards_target()
        # Déposer le pollen à la ruche et réinitialiser le compteur de pollen
        else:
            self.enAlerte = False
            if self.zone_targeted and self.zone_targeted.zone_id[0] == self.hive.position[0] and self.zone_targeted.zone_id[1] == self.hive.position[1]:
                listePlante = self.map.getListePlant(self.grid_position)
                for p in listePlante:
                    if isinstance(p,Plant):
                        
                        if p.IsOccupee or p.onCooldown:
                            self.nbPlantesOccupee += 1
                   
                self.InZoneTargeted = False
            self.deposit_pollen(self.hive)

    def isAtHive(self):
        return (abs(self.home_position[0] - self.pixel_position[0]) < 5 and abs(self.home_position[1] - self.pixel_position[1]) < 5)

    def isAtTarget(self):
        return (abs(self.target_position[0] - self.pixel_position[0]) < 5 and abs(self.target_position[1] - self.pixel_position[1]) < 5)

    def deposit_pollen(self,hive):
        # Déposer le pollen à la ruche
        # Cela pourrait impliquer d'augmenter un compteur dans la ruche ou une autre logique
        hive.store_pollen_from_bee(self.pollen_collected)
        
        if self.pollen_collected <= 0:
            self.go_store = False
            hive.add_to_bee_waiting_list_init(self)
        else:
            if self.notDeposedYet:
                
                hive.give_information(self.nbPlantes, self.nbCarniPlantes, self.nbPlantesOccupee, self.zone_targeted)
                self.notDeposedYet = False
                self.nbPlantesOccupee = 0
                self.nbCarniPlantes = set()
            self.pollen_collected -= 1
            
            
        
    def communicate_flower_location(self, flower_location):
        # Communiquer l'emplacement d'une fleur à d'autres abeilles
        # Cela pourrait impliquer de mettre à jour une sorte de mémoire partagée ou de carte
        pass

    def isOnPlant(self):
        current_zone = pixel_to_grid(self.pixel_position,self.map.zone_width,self.map.zone_height)
        zoneX = int(current_zone[0])
        zoneY = int(current_zone[1])
        print(zoneX)
        print(zoneY)
        for plant in self.map.zones[zoneX][zoneY].plants:
            if(self.pixel_position == plant.position):
                return True
        return False
    
    def die(self):
        self.is_alive = False
        self.grid_position = (-1,-1)
        self.pixel_position = (-100,-100)


    def update(self):
        # Mettre à jour le comportement de l'abeille à chaque tick du jeu
        # Implémenter la logique de décision pour se déplacer, récolter du pollen, etc.
       
            
            
        if self.is_alive:
            if self.go_store:
               
                    
                if self.zone_targeted and not(self.zone_targeted.analyseZone(self.grid_position)) and self.InZoneTargeted: #Si l'abeille vient de sortir de sa zone targeted
                    
                    realZone = self.map.zones[self.zone_targeted.zone_id[1]][self.zone_targeted.zone_id[0]]
                    realZone.removeBeeFromList(self)
                    listePlante = self.map.getListePlant(self.zone_targeted.zone_id)
                    for p in listePlante:
                        if isinstance(p,Plant):
                            
                            if p.IsOccupee or p.onCooldown:
                                self.nbPlantesOccupee += 1
                   
                    self.InZoneTargeted = False
                self.return_to_hive()
                self.plant = None
            else:
                #if(self.target_position == None):
                    #self.set_target((random.randint(0,1200),random.randint(0,800)))
                #self.map.getPlant(self.target_position)
                
                if self.zone_targeted.analyseZone(self.grid_position) and not(self.InZoneTargeted): #Si l'abeille vient de rentrer dans sa zone targeted
                    
                    
                    
                    realZone = self.map.zones[self.zone_targeted.zone_id[1]][self.zone_targeted.zone_id[0]]
                    realZone.addBeeInList(self)
                    self.nbPlantes = realZone.nbPlante
                    self.InZoneTargeted = True
                
                
                    
                if not(self.isAtTarget()): # si la bee a pas atteint sa cible
                    self.move_towards_target()
                else:
                    if self.plant: # si la cible est une plante
                        if isinstance(self.plant,Plant): # si elle n'est pas carnivore
                            
                            if self.pollen_collected == self.pollen_capacity: # elle est full
                                self.go_store = True
                            elif self.plant.isOnCD(): # la plante est en CD
                                if self.map.getNbPlantZone(self.grid_position) == 1: # s'il n'y a d'autre plante
                                    self.go_store = True
                                else: # s'il y a une autre plante
                                    self.plant = self.map.getPlant(self.grid_position)
                                    self.set_target(self.plant.get_position())
                            else: # elle est sur une plante et recupere le pollen
                                
                                self.pollen_collected += self.plant.get_pollen()
                        else: # la plante est carnivore
                            if self.plant.get_isEating(): # la plante est en train de manger
                                self.go_store = True
                            else:
                                self.plant.eat_bee(self)
                    else: # la cible est pas une plante (c'est une zone)
                        
                        if self.map.getNbPlantZone(self.grid_position) > 0: # s'il existe des plantes dans la zone
                            self.plant = self.map.getPlant(self.grid_position)
                            self.set_target(self.plant.get_position())
                        else: # pas de plante, on retourne a la ruche
                            self.go_store = True

    def draw_bee(self, window, cell_width, cell_height, image):
        x = self.pixel_position[0]
        y = self.pixel_position[1] 

        img_with_flip = pygame.transform.flip(image, self.direction, False)

        window.blit(img_with_flip, (x, y))