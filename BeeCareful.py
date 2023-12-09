import pygame
import random
from Map import Map  # Assurez-vous que Map est correctement importé
from Bee import Bee
from utils import *
from Hive import Hive

def main():

    # Creating window
    pygame.init()
    window_width = 1200
    window_height = 800
    window = pygame.display.set_mode((window_width, window_height))

    

    # Creating map
    grid_width = 5  # Number of zones on x axis
    grid_height = 5  # Number of zones on y axis
    zone_width = window_width // grid_width
    zone_height = window_height // grid_height
    game_map = Map(grid_width, grid_height, zone_width, zone_height)
    game_map.populate_map(10)
    
    # Creating hives
    hive = Hive((3,3),grid_width, grid_height, zone_width, zone_height)
    hive.score_init()
    hive.sort_priority()
    hive.print_priority()
  #  nbPlant = 0
   # print(zone_width,"    ",zone_height)
    for row in game_map.zones:
        for zone in row:
            
            hive.zone_tier_list.append(zone)
            
  #          print("\nzone = ",zone.zone_id)
   #         for plant in zone.plants:
    #            nbPlant += 1
    #            print("plants : ",plant.position,"    ",zone.minX < plant.position[0] and plant.position[0] < zone.maxX,"     ",zone.minY < plant.position[1] and plant.position[1] < zone.maxY)
     #       for carnivorous_plants in zone.carnivorous_plants:
      #          nbPlant += 1
       #         print("carni_plants : ",carnivorous_plants.position,"    ",zone.minX < carnivorous_plants.position[0] and carnivorous_plants.position[0] < zone.maxX,"     ",zone.minY < carnivorous_plants.position[1] and carnivorous_plants.position[1] < zone.maxY)
 #   print(nbPlant)



    # Creating bees
    bees = []

    num_bees = 50

    for _ in range(num_bees):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        xZone, yZone = random.randint(0, zone_width - 1), random.randint(0, zone_height - 1)

        bee = Bee(game_map, [3,3], grid_to_pixel((3,3),zone_width,zone_height), grid_to_pixel((3,3),zone_width,zone_height),hive)

        bees.append(bee)

    # Loading images
    bee_image = pygame.image.load('abeille.png')
    bee_image = pygame.transform.scale(bee_image, (50,50))

    plant_image = pygame.image.load('fleur.png')
    plant_image = pygame.transform.scale(plant_image, (75,75))
    
    plant_image_morte = pygame.image.load('fleur_morte.png')
    plant_image_morte = pygame.transform.scale(plant_image_morte, (75,75))

    carni_plant_image = pygame.image.load('plantecarnivore.png')
    carni_plant_image = pygame.transform.scale(carni_plant_image, (75,75))

    hive_image = pygame.image.load('ruche.png')
    hive_image = pygame.transform.scale(hive_image,(100,100))

    background_image = pygame.image.load('grass.jpg')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))

    hive.zone_priority_list_init()
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(background_image,(0,0))  # Background image
        game_map.draw(window)  # Draw zones
        for row in game_map.zones:
            for zone in row:
                for plant in zone.plants:
                    if not(plant.isOnCD()):
                        plant.draw_plant(window,plant.position,zone_width,zone_height,plant_image) # Draw plants
                    else:
                        plant.draw_plant(window,plant.position,zone_width,zone_height,plant_image_morte)
                for carni_plant in zone.carnivorous_plants:
                    carni_plant.draw_carni_plant(window,carni_plant.position,zone_width,zone_height,carni_plant_image) # Draw plants
        for bee in bees:
            
            if not(bee.isAtHive()):
                bee.draw_bee(window,zone_width,zone_height,bee_image) # Draw bees
            else:
                hive.give_action()
            bee.update()
        hive.draw_hive(window,hive.position,zone_width,zone_height,hive_image) # Draw hives
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
