import pygame
import random
from Map import Map  # Assurez-vous que Map est correctement importé
from Bee import Bee
from utils import *
from Hive import Hive
from Plant import Plant

def main():

    # Creating window
    pygame.init()
    
    bandeau_height = 40
    bandeau_color = (255, 233, 72)  # Bleu foncé, par exemple
    
    
    window_width = 1600
    window_height = 900
    window = pygame.display.set_mode((window_width, window_height + bandeau_height))
    pygame.display.set_caption("Bee Careful")
    
    

    # Creating map
    grid_width = 5  # Number of zones on x axis
    grid_height = 5  # Number of zones on y axis
    zone_width = window_width // grid_width
    zone_height = window_height // grid_height
    game_map = Map(grid_width, grid_height, zone_width, zone_height)
    game_map.populate_map(24)
    
    # Creating hives
    hive = Hive((3,3),grid_width, grid_height, zone_width, zone_height,1)
    hive.score_init()
    hive.sort_priority()
    
    hive_2 = Hive((1,1),grid_width, grid_height, zone_width, zone_height,2)
    hive_2.score_init()
    hive_2.sort_priority()
    
  
    for row in game_map.zones:
        for zone in row:
            
            hive.zone_tier_list.append(zone)
            hive_2.zone_tier_list.append(zone)
    



    # Creating bees
    bees = []



    num_bees = 50


    for _ in range(num_bees):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        xZone, yZone = random.randint(0, zone_width - 1), random.randint(0, zone_height - 1)

        bee = Bee(game_map, [3,3], grid_to_pixel((3,3),zone_width,zone_height), grid_to_pixel((3,3),zone_width,zone_height),hive)
        bees.append(bee)
        bee = Bee(game_map, [1,1], grid_to_pixel((1,1),zone_width,zone_height), grid_to_pixel((1,1),zone_width,zone_height),hive_2)
        bees.append(bee)

    # Loading images
    bee_image = pygame.image.load('../images/abeille.png')
    bee_image = pygame.transform.scale(bee_image, (50,50))
    pygame.display.set_icon(bee_image)

    bee_image_alerte = pygame.image.load('../images/abeille_en_alerte.png')
    bee_image_alerte = pygame.transform.scale(bee_image_alerte, (75,75))
    
    pink_bee_image = pygame.image.load('../images/pink_bee.png')
    pink_bee_image = pygame.transform.scale(pink_bee_image, (75,75))

    pink_bee_image_alerte = pygame.image.load('../images/pink_bee_alerte.png')
    pink_bee_image_alerte = pygame.transform.scale(pink_bee_image_alerte, (75,75))

    plant_image = pygame.image.load('../images/fleur.png')
    plant_image = pygame.transform.scale(plant_image, (75,75))
    
    plant_image_morte = pygame.image.load('../images/fleur_morte.png')
    plant_image_morte = pygame.transform.scale(plant_image_morte, (75,75))

    carni_plant_image = pygame.image.load('../images/plantecarnivore.png')
    carni_plant_image = pygame.transform.scale(carni_plant_image, (75,75))

    carni_plant_image_crous = pygame.image.load('../images/plantecarnivoreSadgeCrous.png')
    carni_plant_image_crous = pygame.transform.scale(carni_plant_image_crous, (75,75))

    carni_plant_image_crous_pink = pygame.image.load('../images/plantecarnivoreSadgeCrous_pink.png')
    carni_plant_image_crous_pink = pygame.transform.scale(carni_plant_image_crous_pink, (75,75))

    hive_image = pygame.image.load('../images/ruche.png')
    hive_image = pygame.transform.scale(hive_image,(100,100))
    
    hive_2_image = pygame.image.load('../images/ruche_2.png')
    hive_2_image = pygame.transform.scale(hive_2_image,(100,100))

    background_image = pygame.image.load('../images/grass.jpg')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))


    score_font = pygame.font.Font("../fonts/Grand9K_Pixel.ttf", 30)
    

    # Game loop
    running = True
    while running:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(background_image,(0,0))  # Background image
        #game_map.draw(window)  # Draw zones
        
        for row in game_map.zones:
            for zone in row:
                zone.update()
                for plant in zone.listPlantTotal:
                    plant.update()  
                    if(isinstance(plant,Plant)):  
                        if not(plant.isOnCD()):
                            plant.draw_plant(window,plant.position,zone_width,zone_height,plant_image) # Draw plants
                        else:
                            plant.draw_plant(window,plant.position,zone_width,zone_height,plant_image_morte)
                    else:
                        if plant.get_isEating():
                            if plant.get_couleurAbeille() == 1:
                                plant.draw_carni_plant(window,plant.position,zone_width,zone_height,carni_plant_image_crous) # Draw plants
                            else:
                                plant.draw_carni_plant(window,plant.position,zone_width,zone_height,carni_plant_image_crous_pink) # Draw plants
                        else:
                            plant.draw_carni_plant(window,plant.position,zone_width,zone_height,carni_plant_image) # Draw plants
        nbPink = 0
        nbYellow = 0
        for bee in bees:
            if bee.is_alive:
                if bee.get_hive() == 1:
                    nbYellow += 1
                if bee.get_hive() == 2:
                    nbPink += 1
            if(bee.is_alive):
                if not(bee.isAtHive()):
                    if not(bee.isEnAlerte()):
                        if bee.hive == hive:
                            bee.draw_bee(window,zone_width,zone_height,bee_image) # Draw bees
                        else:
                            bee.draw_bee(window,zone_width,zone_height,pink_bee_image) # Draw bees
                    else:
                        if bee.hive == hive:
                            bee.draw_bee(window,zone_width,zone_height,bee_image_alerte) # Draw bees
                        else:
                            bee.draw_bee(window,zone_width,zone_height,pink_bee_image_alerte) # Draw bees
                else:
                    hive.give_action()
                    hive_2.give_action()
            bee.update()
        
        hive_2.draw_hive(window,hive_2.position,zone_width,zone_height,hive_2_image) # Draw hives
        hive.draw_hive(window,hive.position,zone_width,zone_height,hive_image) # Draw hives
        
        
        pygame.draw.rect(window, bandeau_color, [0, window_height , window_width, window_width + bandeau_height])
        score_text_hive_1 = score_font.render(f" {nbPink} # Score : {hive_2.stored_pollen // 100}", True, (0, 0, 0))
        score_text_hive_2 = score_font.render(f" {nbYellow} # Score : {hive.stored_pollen // 100}", True, (0, 0, 0))
        
        temp_surface = pygame.Surface((window_width // 2,bandeau_height))
        temp_surface.fill(bandeau_color)
        temp_surface.blit(score_text_hive_1,(250,0))
        temp_surface.blit(pink_bee_image,(192,-17))
        
        temp_surface_2 = pygame.Surface((window_width // 2,bandeau_height))
        temp_surface_2.fill(bandeau_color)
        temp_surface_2.blit(score_text_hive_2,(window_width // 2 - 450,0))
        temp_surface_2.blit(bee_image,(window_width // 2 - 498,-5))
        
        
        window.blit(temp_surface, (0,window_height + bandeau_height - score_text_hive_2.get_height() ))  # Positionnez comme nécessaire
        window.blit(temp_surface_2, (window_width // 2, window_height + bandeau_height - score_text_hive_2.get_height() ))  # Positionnez comme nécessaire
        

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()