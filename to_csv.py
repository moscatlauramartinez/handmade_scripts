# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:59:51 2024

@author: lerin
"""

import re
import csv


def extract_data(linea): # extracts the numbers and words from a line
    # find numbers and words with a regular expression
    palabras_y_numeros = re.findall(r"(?:[^\s]+)|(?:[-+]?\d*\.\d+e[-+]?\d+)|(?:[-+]?\d*\.\d+)|(?:\d+)", linea)
    # return them
    return palabras_y_numeros

def matrixdata_to_float(matriz): # converts de data to float numers (decimals)
    #iterate each line of the matrix
    for fila in matriz:
        # iterate each line of the matrix (put in the number the index in wich start tho change from string to float)
        for i in range(0, len(fila)):
            # change the format
            fila[i] = float(fila[i])
    # return the matrix
    return matriz


def extract_headers (file_path): # takes the headers of the file
    # open the input file (only with read permissions)
    f = open(file_path, "rt")
    # create the vector to fill with headers
    headers = []
    # iterate each line of the file
    for line in f:
        # find the headers lines
        if line[0:6] == '# name':
            # accumulate headers in the headers vector
            headers.append(line[11:].strip())
    # close the file
    f.close()
    return(headers)

def extract_matrix (file_path): # takes the data of the file (with no headers)
    # open the input file (only with read permissions)
    f = open(file_path, "rt")
    # create the matrix to fill with numbers
    data_matrix = []
    #iterate each line of the file
    for line in f:
        # find the lines with data
        if line[0:4] == '    ':
            # extract the data in a vector called dades
            dades = extract_data(line)
            # append the vector to the matrix
            data_matrix.append(dades)
    # convert the data to float (decimal numbers)
    float_data_matrix = matrixdata_to_float(data_matrix)
    # close the file
    f.close()
    return(float_data_matrix)

def generate_csv_from_data_and_headers (name_new_csv, data_matrix, headers):
    # create a csv in the specified path with write permissions
    with open(name_new_csv, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # write the headers
        escritor_csv.writerow(headers)
        # write the data
        for fila in data_matrix:
            escritor_csv.writerow(fila)
            
def generate_csv_from_sbe_file(input_path, output_path):
    headers = extract_headers(input_path)
    data = extract_matrix(input_path)
    generate_csv_from_data_and_headers(output_path, data, headers)
    

# put here the input file path
file_path = r'C:\Users\lerin\Desktop\campanya_locate\test2\6_csv_excels\data\2024-05-06T150546_SBE0251182CTD.cnv'

# put here the outout file path
new_csv = r'C:\Users\lerin\Desktop\campanya_locate\test2\6_csv_excels\analysis\proc_2024-05-06T150546_SBE0251182CTD.cnv'

generate_csv_from_sbe_file(file_path, new_csv)