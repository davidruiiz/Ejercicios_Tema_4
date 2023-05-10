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

