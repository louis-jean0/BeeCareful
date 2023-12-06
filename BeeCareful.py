import pygame
import random
from Map import Map  # Assurez-vous que Map est correctement importé
from Bee import Bee

def main():
    pygame.init()
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))

    grid_width = 5  # Nombre de zones en largeur
    grid_height = 5  # Nombre de zones en hauteur
    zone_width = window_width // grid_width
    zone_height = window_height // grid_height

    background_image = pygame.image.load('grass.jpg')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))


    game_map = Map(grid_width, grid_height, zone_width, zone_height)
    game_map.populate_map(10,2)

    bees = []
    num_bees = 100
    for _ in range(num_bees):
        x, y = random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)
        bee = Bee([x,y], [270,270], (0,0))
        bees.append(bee)

    bee_image = pygame.image.load('abeille.png')
    bee_image = pygame.transform.scale(bee_image, (50,50))

    plant_image = pygame.image.load('fleur.png')
    plant_image = pygame.transform.scale(plant_image, (75,75))

    # Boucle de jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(background_image,(0,0))  # Fond noir
        game_map.draw(window)  # Dessiner la carte
        for row in game_map.zones:
            for zone in row:
                for plant in zone.plants:
                    plant.draw_plant(window,plant.position,zone_width,zone_height,plant_image)
        for bee in bees:
            bee.draw_bee(window,zone_width,zone_height,bee_image)
            bee.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
