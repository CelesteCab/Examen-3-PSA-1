arrEntrada = []
arrSalida = []
global salida
global cant
salida = ""
cant = 0

#texto = input('Ingrese la cadena')

path = 'text.txt'

dict = {}

with open(path, 'r') as file:
    for line in file:
        key, value = map(str.strip, line.split('='))

        dict[key] = value

# Función para encriptar la cadena
def encriptar(texto):
    resultado = []
    for caracter in texto:
        # Si el caracter está en el diccionario de encriptación, reemplazar, de lo contrario, usar 'N'
        resultado.append(dict.get(caracter, 'N'))
    return resultado


texto = input('Ingrese la cadena')
salida = encriptar(texto)

print('salida: ' , salida)
print('longitud: ' , len(salida))