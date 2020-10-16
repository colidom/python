import usuarios.usuario as modelo

class Acciones:

    def registro(self):
            print("\nOK!!! Vamos a registrate en el sistema...")
            nombre = input("¿Cual es tu nombre?: ")
            apellidos = input("¿Cuales son tus apellidos?: ")
            email = input("¿Cual es tu email?: ")
            password = input("¿Cual es tu contraseña?: ")
    
            usuario = modelo.Usuario(nombre, apellidos, email, password)
            registro = usuario.registrar()

            if registro[0] >= 1:
                print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            else:
                print("\nNo te has registrado correectamente !!!")

    def login(self):
        print("Vale!!! Identifícate en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        password = input("¿Cual es tu contraseña?: ")
        