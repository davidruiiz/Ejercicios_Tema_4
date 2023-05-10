import random

class Misión:
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general
        self.recursos_asignados = {}