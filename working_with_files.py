#!/usr/bin/python3
# @author Carlos
# v1.1
# importing  modules
import os
import shutil

# Ruta actual de los ficheros de entrada
srcpath = input('Por favor indique la ruta de los ficheros de entrada: ')or 'C:\\Users\\A704806\\Desktop\\MONITORIZACION\\coger'
dest = input('Por favor indica la ruta para dejar los ficheros: ') or 'C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar'
os.chdir(dest)

#Comprobamos los tópicos en los archivos y creamos las correspondientes carpetas
for f in os.listdir(srcpath):
    splitname = f.split('_')
    foldername = splitname[2]
    if not os.path.exists(foldername):
        os.mkdir(foldername)

# #COPIAMOS los ficheros a su carpeta correspondiente
for filename in os.listdir(srcpath):
    root, ext = os.path.splitext(filename)
    if 'AMAZON' in filename:
        amazon = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\AMAZON')
        shutil.copy(os.path.join(srcpath, filename), amazon)
    elif 'INTERBOX' in filename:
        interbox = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\INTERBOX')
        shutil.copy(os.path.join(srcpath, filename), interbox)
    elif 'TRAN' in filename:
        tran = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\TRAN')
        shutil.copy(os.path.join(srcpath, filename), tran)
    elif 'UNICO' in filename:
        unico = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\UNICO')
        shutil.copy(os.path.join(srcpath, filename), unico)
    elif 'ICP_WS' in filename:
        icp = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\ICP')
        shutil.copy(os.path.join(srcpath, filename), icp)
    elif 'OPENBANK' in filename:
        openbank = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\OPENBANK')
        shutil.copy(os.path.join(srcpath, filename), openbank)
    elif 'EMSEVT' in filename:
        emsevt = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\EMSEVT')
        shutil.copy(os.path.join(srcpath, filename), emsevt)
    elif 'EVT' in filename:
        evt = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\EVT')
        shutil.copy(os.path.join(srcpath, filename), evt)
    elif 'VDFNE' in filename :
        vdfne = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\VDFNE')
        shutil.copy(os.path.join(srcpath, filename), vdfne)
