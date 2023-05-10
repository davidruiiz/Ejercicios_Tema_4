import random

class Misión:
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general
        self.recursos_asignados = {}

class GrafoMisiones:
    def __init__(self):
        self.nodos = []
        self.aristas = {}

    def agregar_nodo(self, misión):
        self.nodos.append(misión)

    def agregar_arista(self, origen, destino):
        if origen not in self.aristas:
            self.aristas[origen] = []
        self.aristas[origen].append(destino)

    def prioridad_misión(self, misión):
        if misión.general == "Palpatine" or misión.general == "Darth Vader":
            return "alta"
        else:
            return "baja"
        
    def asignar_recursos(self, misión):
        prioridad = self.prioridad_misión(misión)
        if prioridad == "alta":
            print("Asignar recursos manualmente para la misión {} en el planeta {}.".format(misión.tipo, misión.planeta))
        else:
            if misión.tipo == "exploración":
                misión.recursos_asignados["Scout Troopers"] = 15
                misión.recursos_asignados["speeder bike"] = 2
            elif misión.tipo == "contención":
                misión.recursos_asignados["Stormtroopers"] = 30
                vehículos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
                for i in range(3):
                    misión.recursos_asignados[random.choice(vehículos)] = 1
            elif misión.tipo == "ataque":
                misión.recursos_asignados["Stormtroopers"] = 50
                vehículos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
                for i in range(7):
                    misión.recursos_asignados[random.choice(vehículos)] = 1

    def mostrar_recursos(self):
        total_recursos = {}
        for misión in self.nodos:
            print("Misión {} en el planeta {} solicitada por {}:".format(misión.tipo, misión.planeta, misión.general))
            print("Prioridad:", self.prioridad_misión(misión))
            print("Recursos asignados:")
            for recurso, cantidad in misión.recursos_asignados.items():
                print("- {} : {}".format(recurso, cantidad))
                if recurso not in total_recursos:
                    total_recursos[recurso] = 0
                total_recursos[recurso] += cantidad
            print()
        print("Total de recursos asignados:")
        for recurso, cantidad in total_recursos.items():
            print("- {} : {}".format(recurso, cantidad))

    def mostrar_misiones(self):
        for misión in self.nodos:
            print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
            print("Recursos asignados:")
            for recurso, cantidad in misión.recursos_asignados.items():
                print("- {} : {}".format(recurso, cantidad))
            print()

    def mostrar_misiones_planeta(self, planeta):
        for misión in self.nodos:
            if misión.planeta == planeta:
                print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
                print("Recursos asignados:")
                for recurso, cantidad in misión.recursos_asignados.items():
                    print("- {} : {}".format(recurso, cantidad))
                print()

    def mostrar_misiones_general(self, general):
        for misión in self.nodos:
            if misión.general == general:
                print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
                print("Recursos asignados:")
                for recurso, cantidad in misión.recursos_asignados.items():
                    print("- {} : {}".format(recurso, cantidad))
                print()

    def mostrar_misiones_tipo(self, tipo):
        for misión in self.nodos:
            if misión.tipo == tipo:
                print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
                print("Recursos asignados:")
                for recurso, cantidad in misión.recursos_asignados.items():
                    print("- {} : {}".format(recurso, cantidad))
                print()

    def mostrar_misiones_prioridad(self, prioridad):
        for misión in self.nodos:
            if self.prioridad_misión(misión) == prioridad:
                print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
                print("Recursos asignados:")
                for recurso, cantidad in misión.recursos_asignados.items():
                    print("- {} : {}".format(recurso, cantidad))
                print()

    def mostrar_misiones_recursos(self, recurso):
        for misión in self.nodos:
            if recurso in misión.recursos_asignados:
                print("Misión {} en el planeta {} solicitada por {}.".format(misión.tipo, misión.planeta, misión.general))
                print("Recursos asignados:")
                for recurso, cantidad in misión.recursos_asignados.items():
                    print("- {} : {}".format(recurso, cantidad))
                print()

grafo_misiones = GrafoMisiones()

m1 = Misión("exploración", "Tatooine", "Palpatine")
m2 = Misión("contención", "Tatooine", "Darth Vader")
m3 = Misión("ataque", "Tatooine", "Darth Vader")
m4 = Misión("exploración", "Naboo", "Palpatine")
m5 = Misión("contención", "Naboo", "Darth Vader")
m6 = Misión("ataque", "Naboo", "Darth Vader")

grafo_misiones.agregar_nodo(m1)
grafo_misiones.agregar_nodo(m2)
grafo_misiones.agregar_nodo(m3)
grafo_misiones.agregar_nodo(m4)
grafo_misiones.agregar_nodo(m5)
grafo_misiones.agregar_nodo(m6)

grafo_misiones.agregar_arista(m1, m2)
grafo_misiones.agregar_arista(m1, m3)
grafo_misiones.agregar_arista(m2, m5)
grafo_misiones.agregar_arista(m3, m6)

