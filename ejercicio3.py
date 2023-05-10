class Vertex:  # Clase que representa un vértice del grafo
    def __init__(self, name, v_type):
        self.name = name
        self.v_type = v_type
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=1): # Añade un vecino al vértice
        self.adjacent[neighbor] = weight

    def get_connections(self): # Devuelve los vecinos del vértice
        return self.adjacent.keys()

    def __str__(self): # Devuelve el nombre del vértice y sus vecinos
        return f"{self.name}: {self.adjacent}"


class Graph:  # Clase que representa el grafo
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, name, v_type): # Añade un vértice al grafo
        self.num_vertices += 1
        new_vertex = Vertex(name, v_type)
        self.vert_dict[name] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, weight=1): # Añade una conexión entre dos vértices
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], weight)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], weight)

    def dijkstra(self, start, target): # Algoritmo de Dijkstra
        import heapq

        dist = {vertex: float('infinity') for vertex in self.vert_dict}
        dist[start] = 0

        pq = [(0, start)]

        while pq: # Mientras la cola de prioridad no esté vacía
            cur_dist, cur_vertex = heapq.heappop(pq) # Extrae el vértice con menor distancia

            if cur_dist > dist[cur_vertex]:  # Si la distancia extraída es mayor que la distancia del vértice actual
                continue # Se pasa al siguiente vértice

            for neighbor, weight in self.vert_dict[cur_vertex].adjacent.items(): # Para cada vecino del vértice actual
                distance = cur_dist + weight # Se calcula la distancia

                if distance < dist[neighbor.name]: # Si la distancia calculada es menor que la distancia del vecino
                    dist[neighbor.name] = distance # Se actualiza la distancia del vecino
                    heapq.heappush(pq, (distance, neighbor.name)) # Se añade el vecino a la cola de prioridad 

        return dist[target] # Se devuelve la distancia del objetivo

# Creación del grafo y de sus vértices
g = Graph()

stations = ["King's Cross", "Waterloo", "Victoria Train Station", "Liverpool Street Station", "St. Pancras", "Paddington"]
junctions = [str(i) for i in range(1, 13)]

for station in stations:
    g.add_vertex(station, 'station') # Se añaden las estaciones

for junction in junctions:
    g.add_vertex(junction, 'junction') # Se añaden las intersecciones

# Conexiones entre los vértices
g.add_edge("King's Cross", '1') 
g.add_edge('1', '2') 
g.add_edge('2', '3')
g.add_edge('3', 'Waterloo')
g.add_edge('Victoria Train Station', '4')
g.add_edge('4', '5')
g.add_edge('5', '6')
g.add_edge('6', 'Liverpool Street Station')
g.add_edge('St. Pancras', '7')
g.add_edge('7', '8')
g.add_edge('8', "King's Cross")

# Encuentra el camino más corto
print("El camino más corto para ir de King's Cross a Waterloo:", g.dijkstra("King's Cross", 'Waterloo'))
print("El camino más corto para ir de Victoria Train Station a Liverpool Street Station:", g.dijkstra('Victoria Train Station', 'Liverpool Street Station'))
print("El camino más corto para ir de St. Pancras a King's Cross:", g.dijkstra('St. Pancras', "King's Cross"))


