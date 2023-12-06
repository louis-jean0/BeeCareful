from Plant import Plant

class CarnivorousPlant(Plant):
    
    def __init__(self,range):
        self.nb_bees_eaten = 0
        self.range = range