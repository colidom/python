# !/usr/bin/python3
# importing  modules
import os
import shutil

# Ruta actual de los ficheros de entrada
os.chdir('C:\\Users\\A704806\\Desktop\\files')
srcpath = ('C:\\Users\\A704806\\Documents\\SOA\\MONITORIZACION\\20190414_ficheros_salida.tar\\TRAN\\2')



for file in os.listdir(srcpath):
    foldername = file[11:-25]
    if not os.path.exists(foldername):
        os.mkdir(foldername)
        shutil.copy(os.path.join(srcpath, file), foldername)
    else:
        shutil.copy(os.path.join(srcpath, file), foldername)
