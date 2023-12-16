# Definir el diccionario de encriptación
encriptacion = {
    'L': '$', 'V': '%', 'E': 'R', 'B': 'Y',
    'A': '7', 'i': '#', 'S': 'Q', 'D': '&',
    'l': '$', 'v': '%', 'e': 'R', 'b': 'Y',
    'a': '7', 'i': '#', 's': 'Q', 'd': '&'
}

# Función para encriptar la cadena
def encriptar(cadena):
    resultado = []
    for caracter in cadena:
        # Si el caracter está en el diccionario de encriptación, reemplazar, de lo contrario, usar 'N'
        resultado.append(encriptacion.get(caracter, 'N'))
    return resultado

# Leer la cadena desde un archivo
archivo_entrada = "entrada.txt"

try:
    with open(archivo_entrada, "r") as archivo:
        entrada = archivo.read()
except FileNotFoundError:
    print(f"El archivo {archivo_entrada} no fue encontrado.")
    exit()

# Encriptar la cadena
salida = encriptar(entrada)

# Mostrar la salida en pantalla
print("Salida del Sistema:")
print("".join(salida))

# Mostrar la cantidad de caracteres
print("Cantidad de caracteres:", len(salida))

# Guardar la conversión en un archivo
archivo_salida = "salida.txt"
with open(archivo_salida, "w") as archivo:
    archivo.write("".join(salida))

print(f"El resultado se ha guardado en el archivo '{archivo_salida}'")