#!/usr/bin/python3
# @author Carlos
# v2.0
# Importing  modules
import os
import shutil
import sys

# Path for input and output files
srcpath = input('Por favor indique la ruta de los ficheros de entrada: ')
dest = input('Por favor indique la ruta para dejar los ficheros: ')

if srcpath:
    print('La ruta de entrada es: ' + srcpath)
else:
    sys.exit('¡Debe indicar una ruta de entrada! Finalizando programa...')
if dest:
     print('La ruta de salida es: ' + dest)
else:
    sys.exit('¡Debe indicar una ruta de salida! Finalizando programa...')
print('Clasificando ficheros...')
os.chdir(dest)

# Create folders by file name, and then move the files to the corresponding folder
def clasifica():
    for f in os.listdir(srcpath):
        splitname = f.split('_')
        foldername = splitname[2]
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        shutil.move(os.path.join(srcpath, f), foldername)
    return
clasifica()
print('¡Finalizado!')
