import json

#Lee el archivo JSON
with open('futbol.json', 'r') as file:
    data = json.load(file)

#Modifica los datos
data["name"] = "Nuevo Nombre"
data["position"] = "Nueva Posicion"
data["nationality"] = "Nueva Nacionalidad"

#Guarda los cambios en el archivo
with open('archivo_modificado.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Archivo modificado y guardado correctamente.")
