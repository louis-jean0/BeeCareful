class Hive:
    
    def __init__(self, position):
        self.position = position  # Position de la ruche sur la grille
        self.stored_pollen = 0  # Quantité actuelle de pollen stocké
        self.shared_memory = []
        self.bee_waiting_list = []  # Liste d'abeilles en attente d'instructions
        self.zone_tier_list = []    # Liste de priorité des zones
        self.bee_zone_list = []     # Liste de tuple (bee,zone,time) associant une abeille, sa zone ainsi que le temps qu'elle met, incrémenter dans updates()

    def store_pollen_from_bee(self, amount):
        # Ajouter du pollen au stockage, sans dépasser la capacité
        self.stored_pollen += amount

    def update(self):
        # Mettre à jour la ruche à chaque tick du jeu
        # Cela pourrait inclure des actions comme la production de nouvelles abeilles
        pass

    def wait_order(self,bee):
        # Fonction appelé par une abeille lorsqu'elle attend une action
        self.bee_waiting_list.append(bee)
        
    def give_action(self):
        # Donne une action à la 1ère abeille dans la liste

    def draw_hive(self, window, position, zone_width, zone_height, image):
        x = position[0] * zone_width
        y = position[1] * zone_height
        window.blit(image,(x,y))