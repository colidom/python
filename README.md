## Python

*Este repositorio contiene aplicaciones creadas en el lenguaje de programación Python.*

# Contenido del repositorio:

## Flask-Web
 Aplicación web con Flask
 ---
 Proyecto web personal desarrollado con Python3 y el framework Flask.
 (En desarrollo...)

--- 
 
 ## Files-Clasifier
 ### WorkingWithFiles.py
 Herramienta para tratar ficheros clasificándolos en distintos directorios dependiendo del nombre de cada fichero.
 Básicamente hacemos un split del nombre de los ficheros(requerido), mediante "_" de modo que si tuvieramos un 
 fichero con el nombre `11/05/2019_2_AMAZON_invoice_8909282.xml` independientemente de la opción que elijamos, cambiar 
 el nombre de los ficheros o mantener el original, se creará la carpeta `AMAZON_Status_2`:
 
 - Opción 1: Se mueve el fichero a la carpeta ej: `AMAZON_Status_2` manteniendo el nombre original 
 `11052019_2_AMAZON_invoice_8909282.xml`.
 - Opción 2: Se mueve el fichero a la carpeta ej: `AMAZON_Status_2` renombrando el nombre de cada uno de los ficheros 
 de forma correlativa, ej: `Message_0`,`Message_1`, `Message_2`, etc...
--- 
## Utilidades
- agenda.py
    - Con agenda.py donde podemos guardar nombres de contactos con sus respectivos números de teléfono, además de opciones como, mostrar lista de contactos, editar o eliminar un contacto.
- sorteo.py
    - Con sorteo.py podemos realizar sorteos mediante el nombre de los usuarios que nos pedirá el programa mediante la opción uno.
--- 