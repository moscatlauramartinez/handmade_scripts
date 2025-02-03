# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:02:46 2024

@author: lerin
"""

import csv
import re
import os

def obtener_rutas_archivos(directorio):
    archivos = []
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_completa):
            archivos.append(ruta_completa)
    return archivos

def extraer_numeros(linea):
    # Utilizamos una expresión regular para encontrar todas las palabras y números en la línea
    palabras_y_numeros = re.findall(r"(?:[^\s]+)|(?:[-+]?\d*\.\d+e[-+]?\d+)|(?:[-+]?\d*\.\d+)|(?:\d+)", linea)
    # Devolvemos la lista de palabras y números encontrados
    return palabras_y_numeros

def convertir_matriz_a_float(matriz):
    for fila in matriz:
        for i in range(2, len(fila)):
            fila[i] = float(fila[i])
    return matriz

def matrix_csv (nombre_archivo_csv, data_matrix, headers):
    # Escribir los datos en el archivo CSV
    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribir los nombres de las columnas como encabezados
        escritor_csv.writerow(headers)
        # Escribir los datos de la data_matrix en el archivo CSV
        for fila in data_matrix:
            escritor_csv.writerow(fila)

# PUT HERE THE PATH WHERE THE SBE FILES ARE
directorio = r'C:\Users\lerin\Desktop\FARDWO\Terbolesa_nivell_pro\processings\test3_mitjanes1\data'
# Get the paths of all files in the specified directory
carpeta = obtener_rutas_archivos(directorio)
print(carpeta)

headers = []
data_matrix = []
# Loop through each file path in the directory
for path in carpeta:
    # Open the file in text mode
    f = open(path, "rt")
    for line in f:
        # Extract station name from the line starting with '* FileName ='
        if line[0:12] == '* FileName =':
            station = line[74:83]
        # Extract headers from lines starting with '# name'
        if line[0:6] == '# name':
            headers.append(line[11:].strip())
        # Extract data from lines that start with spaces
        if line[0:4] == '    ':
            dades = extraer_numeros(line)
            # Insert the station name at the beginning of the data
            dades.insert(0, station)
            # Add the data to the data matrix
            data_matrix.append(dades)
    # Close the file after reading
    f.close()
# Add the 'station' header at the beginning of the headers list
headers.insert(0, 'station')

# Convert all numerical values in the data matrix to floats
float_data_matrix = convertir_matriz_a_float(data_matrix)

# Define the path where the consolidated CSV file will be saved
csv_totes = r'C:\Users\lerin\Desktop\FARDWO\Terbolesa_nivell_pro\processings\test3_mitjanes1\analysis\totes.txt'
# Write the data matrix and headers to the CSV file
matrix_csv(csv_totes, float_data_matrix, headers)
