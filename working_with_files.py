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
    if filename.__contains__('_AMAZON_'):
        shutil.move(os.path.join(srcpath, filename), amazon)
    elif filename.__contains__('_TRAN'):
        shutil.move(os.path.join(srcpath, filename), tran)
    elif filename.__contains__('_ICP_WS_'):
        shutil.move(os.path.join(srcpath, filename), icp)
    elif filename.__contains__('UNICO'):
        shutil.move(os.path.join(srcpath, filename), unico)
    elif filename.__contains__('OPENBANK'):
        shutil.move(os.path.join(srcpath, filename), openbank)
    elif filename.__contains__('EMSEVT'):
        shutil.move(os.path.join(srcpath, filename), emsevt)
    elif filename.__contains__('EVT'):
        shutil.move(os.path.join(srcpath, filename), evt)
    elif filename.__contains__('INTERBOX'):
        shutil.move(os.path.join(srcpath, filename), interbox)

