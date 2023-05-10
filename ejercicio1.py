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

huffman_tree = crear_arbol_huffman(frecuencias) # Arbol de Huffman
huffman_codes = dict(huffman_tree) # Diccionario de codigos de Huffman

# Mensajes a descodificar
mensaje1 = "100010111010110000101110100011100000110110000001111001111010010110000110100111001101000101110101111111010000111100111111001111010001100011000000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011110111111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100011001011010111001100111101000110001100000010110101111100111001"
mensaje2 = "100010111010110000101110100011100000110110000001111001111010010110000110100111001101000101110101111111010000111100111111001111010001100011000000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100011001011010111001100111101000110001100000010110101111100111001"


# Decodificar mensaje
def decodificar_mensaje(mensaje, huffman_codes):
    mensaje_decodificado = ""
    codigo = ""
    for bit in mensaje:
        codigo += bit
        if codigo in huffman_codes:
            caracter = huffman_codes[codigo]
            mensaje_decodificado += caracter
            codigo = ""
    return mensaje_decodificado

print("Mensaje 1: ", decodificar_mensaje(mensaje1, huffman_codes))
print("Mensaje 2: ", decodificar_mensaje(mensaje2, huffman_codes))

# Espacio memoria

def calcular_espacio_memoria(mensaje_original, mensaje_comprimido):
    espacio_original = len(mensaje_original) * 8  # 8 bits por cada caracter
    espacio_comprimido = len(mensaje_comprimido)
    return espacio_original, espacio_comprimido

print("Espacio de memoria mensaje 1: ", calcular_espacio_memoria(mensaje1, huffman_codes))
print("Espacio de memoria mensaje 2: ", calcular_espacio_memoria(mensaje2, huffman_codes))

# Eficiencia
def calcular_porcentaje_compresion(mensaje_original, mensaje_comprimido):
    espacio_original, espacio_comprimido = calcular_espacio_memoria(mensaje_original, mensaje_comprimido)
    porcentaje_compresion = (espacio_original - espacio_comprimido) / espacio_original * 100
    return porcentaje_compresion

porcentaje_compresion_mensaje1 = calcular_porcentaje_compresion(mensaje1, mensaje1)
porcentaje_compresion_mensaje2 = calcular_porcentaje_compresion(mensaje2, mensaje2)

print("Porcentaje de compresion mensaje 1: ", porcentaje_compresion_mensaje1)
print("Porcentaje de compresion mensaje 2: ", porcentaje_compresion_mensaje2)
