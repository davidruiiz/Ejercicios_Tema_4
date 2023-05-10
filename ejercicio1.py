import heapq
from collections import defaultdict

#Tabla de frecuencias
caracter_cantidad = {
    'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3, 'I': 6, 'L': 6,
    'M': 3, 'N': 6, 'O': 7, 'P': 4, 'Q': 1, 'R': 10, 'S': 4, 'T': 3,
    'U': 4, 'V': 2, ' ': 17, ',': 2
}

# Calcular frecuencias
total_caracteres = sum(caracter_cantidad.values())
frecuencias = {caracter: cantidad / total_caracteres for caracter, cantidad in caracter_cantidad.items()}

#Arbol de Huffman

def crear_arbol_huffman(frecuencias):
    heap = [[peso, [caracter, ""]] for caracter, peso in frecuencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))