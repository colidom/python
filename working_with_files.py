# !/usr/bin/python3
# importing  modules
import os
import shutil

# Ruta actual de los ficheros de entrada
os.chdir('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar')
srcpath = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\coger')
dest = ('C:\\Users\\A704806\\Desktop\\files\\')
os.mkdir('AMAZON')
amazon = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\AMAZON')
os.mkdir('TRAN')
tran = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\TRAN')
os.mkdir('UNICO')
unico = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\UNICO')
os.mkdir('ICP_WS')
icp = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\ICP_WS')
os.mkdir('OPENBANK')
openbank = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\OPENBANK')
os.mkdir('EMSEVT')
emsevt = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\EMSEVT')
os.mkdir('EVT')
evt = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\EVT')
os.mkdir('INTERBOX')
interbox = ('C:\\Users\\A704806\\Desktop\\MONITORIZACION\\dejar\\INTERBOX')

for filename in os.listdir(srcpath):
    root, ext = os.path.splitext(filename)
    if '_AMAZON_' in filename:
        shutil.move(os.path.join(srcpath, filename), amazon)
    elif '_TRAN' in filename:
        shutil.move(os.path.join(srcpath, filename), tran)
    elif '_ICP_WS_' in filename:
        shutil.move(os.path.join(srcpath, filename), icp)
    elif 'UNICO' in filename:
        shutil.move(os.path.join(srcpath, filename), unico)
    elif 'OPENBANK' in filename:
        shutil.move(os.path.join(srcpath, filename), openbank)
    elif 'EMSEVT' in filename:
        shutil.move(os.path.join(srcpath, filename), emsevt)
    elif 'EVT' in filename:
        shutil.move(os.path.join(srcpath, filename), evt)
    elif 'INTERBOX' in filename:
        shutil.move(os.path.join(srcpath, filename), interbox)

