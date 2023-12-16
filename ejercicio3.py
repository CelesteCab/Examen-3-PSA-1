import csv
import sys
import pandas as pd

filename='bddpsa.csv'

#Persona con mayor edad
with open(filename, "r", newline="") as csvfile:
	reader = csv.DictReader(csvfile)
	print(max(int(row['edad']) for row in reader))


#Persona con menor edad
with open(filename, "r", newline="") as csvfile:
	reader = csv.DictReader(csvfile)
	print(min(int(row['edad']) for row in reader))


#Cuantas mujeres y hombres
df = pd.read_csv(filename)

print(f"Cantidad Hombres : {len(df[df['genero'] == "Masculino"])}")
print(f"Cantidad Mujeres : {len(df[df['genero'] == "Femenino"])}")


#Salario promedio
salarios = []
with open(filename, "r", newline="") as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		salarios.append(float(row["salario"]))

print("Salario Promedio: ", sum(salarios) / len(salarios))


#Persona con mas deducciones
with open(filename, "r", newline="") as csvfile:
	reader = csv.DictReader(csvfile)
	print(max(int(row['deducciones']) for row in reader))


#Persona que gana mas
with open(filename, "r", newline="") as csvfile:
	reader = csv.DictReader(csvfile)
	print(max(int(row['salario']) for row in reader))