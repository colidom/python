# !/usr/bin/python3
# importing  modules
import os
import shutil

# Function to rename multiple files

# Ruta actual de los ficheros de entrada
allfiles = os.listdir('C:\\Users\\A704806\\Python\\mytest')
filetype = 'Estado_2'

for file in allfiles:
    if file.startswith(filetype):
        print(file)
