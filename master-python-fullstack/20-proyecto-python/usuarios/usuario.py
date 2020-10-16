import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python",
    port = 3306
)

cursor = database.cursor(buffered = True) # Nos permite hacer varias consultas con el mismo cursor

class Usuario():

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):

        # Cifrar contraseña 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
            
    
    def identificar(self):
        return self.nombre

    